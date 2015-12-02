# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db.models import Avg, Sum, Min, Max
from collections import defaultdict, Counter
from usability_tests.models import Scenario
from usability_tests_executions.models import TaskScenarioExecution, Observation
from tasks.models import ObservationType
from .models import ChartCachedData


time_type = ObservationType.objects.get(name='time')


class Chart(object):

    def as_dict(self):
        return {
            'title': self.get_title(),
            'data': self.get_data_as_dict(),
        }

    def get_data_as_dict(self):
        return map(self.item_as_dict, self.get_data())

    def item_as_dict(self, item):
        return item

    def get_title(self):
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()


class BarChart(Chart):
    pass


class StackedBarChart(Chart):

    def get_legends(self):
        raise NotImplementedError()

    def get_stack_names(self):
        raise NotImplementedError()

    def as_dict(self):
        d = super(StackedBarChart, self).as_dict()
        d['legends'] = self.get_legends()
        d['stack_names'] = self.get_stack_names()
        return d


class CompareTaskBetweenVersionsChart(StackedBarChart):

    type_id = 1

    def as_dict(self):
        try:
            cached = ChartCachedData.objects.get(
                type=self.type_id,
                usability_test=self.usability_test,
            )
            return json.loads(cached.data)
        except ChartCachedData.DoesNotExist:
            self._calculate()
            data = super(CompareTaskBetweenVersionsChart, self).as_dict()
            ChartCachedData.objects.create(
                type=self.type_id,
                usability_test=self.usability_test,
                data=json.dumps(data),
            )
            return data

    def __init__(self, usability_test):
        self.usability_test = usability_test

    def _calculate(self):
        obs = Observation.objects.filter(
            step_execution__interaction_step__scenario_task__task__usability_test=self.usability_test,
            observation_type=time_type,
        )

        versions = list(self.usability_test.versions.order_by('id'))

        total_times = defaultdict(lambda: Counter())
        participants_sets = defaultdict(lambda: defaultdict(lambda: set()))
        for o in obs:
            scenario_task = o.step_execution.interaction_step.scenario_task
            total_times[scenario_task.task][scenario_task.scenario.app_version] += o.value
            participant = o.step_execution.task_scenario_execution.scenario_execution.participant
            participants_sets[scenario_task.task][scenario_task.scenario.app_version].add(participant)

        self.data = []
        self.stack_names = []
        self.legend_items = [v.name for v in versions]
        # TODO: sort key should be order, but id does not exist
        for task in sorted(total_times.keys(), key=lambda task: task.name):
            counter = total_times[task]
            sets = participants_sets[task]
            self.stack_names.append(task.name)
            if len(counter.keys()) == len(versions):
                self.data.append({
                    'name': task.name,
                    'values': [counter[app_version] / float(len(sets[app_version]))
                               for app_version in versions],
                })

    def get_title(self):
        return self.usability_test.name

    def get_stack_names(self):
        return self.stack_names

    def get_data(self):
        return self.data

    def get_legends(self):
        return self.legend_items


class ParticipantTimesPerTaskBarChart(BarChart):

    def __init__(self, participant):
        self.participant = participant

    def get_title(self):
        return 'Tareas realizadas por el participante %s' % self.participant.name

    def item_as_dict(self, scenario_task_execution):
        total = 0
        for step in scenario_task_execution.steps.all():
            if not step.interaction_step.is_question:
                for observation in step.observations.filter(observation_type=time_type):
                    total += observation.value

        return {
            'value': total,
            'name': scenario_task_execution.scenario_task.task.name,
        }

    def get_data(self):
        all_objs = TaskScenarioExecution.objects.all()
        return all_objs.filter(scenario_execution__participant=self.participant)


class UsabilityTestTreeChart(BarChart):

    def __init__(self, usability_test):
        self.usability_test = usability_test

    def get_title(self):
        return self.usability_test.name

    def get_data_as_dict(self):
        tree = self.usability_test_tree(self.usability_test)

        def abbreviate_node_names(node):
            max_len = 30
            if len(node['name']) > max_len:
                node['full_name'] = node['name']
                node['name'] = node['name'][:max_len - 3] + "..."
            children = node.get('children', node.get('_children', []))
            for child in children:
                abbreviate_node_names(child)

        abbreviate_node_names(tree)

        return tree

    def usability_test_tree(self, usability_test):
        scenarios = Scenario.objects.filter(app_version__usability_test=usability_test)
        return {
            'name': usability_test.name,
            'children': map(self.scenario_tree, scenarios)
        }

    def scenario_tree(self, scenario):
        scenario_tasks = scenario.tasks.all()
        return {
            'name': scenario.name,
            'children': map(self.scenario_task_tree, scenario_tasks)
        }

    def scenario_task_tree(self, scenario_task):
        refactorings = scenario_task.refactorings.all()
        steps = scenario_task.steps.all()
        name = scenario_task.task.name
        if name.upper().startswith(self.usability_test.name.upper()):
            name = name[len(self.usability_test.name) + 1:]
            if name.upper().startswith("Test ".upper()):
                name = name[len("Test "):]
        return {
            'name': name,
            '_children': [
                {
                    'name': 'Steps',
                    '_children': map(self.step_tree, steps),
                },
                {
                    'name': 'Refactorings',
                    '_children': map(self.refactoring_tree, refactorings),
                },
            ]
        }

    def refactoring_tree(self, refactoring):
        return {
            'name': refactoring.name,
        }

    def step_tree(self, step):
        observations = Observation.objects.filter(step_execution__interaction_step=step)

        if not observations.exists():
            return {
                'name': step.name,
                '_children': [
                    {
                        'name': 'No data',
                    },
                ],
            }

        min_value = observations.aggregate(min=Min('value'))['min']
        max_value = observations.aggregate(max=Max('value'))['max']
        count = observations.count()
        sum_value = observations.aggregate(sum=Sum('value'))['sum']
        avg_value = observations.aggregate(avg=Avg('value'))['avg']

        return {
            'name': step.name,
            '_children': [
                {
                    'name': "Min: %.2f" % min_value,
                },
                {
                    'name': "Max: %.2f" % max_value,
                },
                {
                    'name': "Count: %d" % count,
                },
                {
                    'name': "Sum: %.2f" % sum_value,
                },
                {
                    'name': "Avg: %.2f" % avg_value,
                },
            ],
        }