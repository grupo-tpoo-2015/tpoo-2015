# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict, Counter
from usability_tests_executions.models import TaskScenarioExecution, Observation
from tasks.models import ObservationType


time_type = ObservationType.objects.get(name='time')


class Chart(object):

    def as_dict(self):
        return {
            'title': self.get_title(),
            'items': self.get_items_as_dict(),
        }

    def get_items_as_dict(self):
        return map(self.item_as_dict, self.get_items())

    def item_as_dict(self, item):
        return item

    def get_title(self):
        raise NotImplementedError()

    def get_items(self):
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

    cache = {}

    @classmethod
    def get(cls, usability_test):
        if usability_test.id not in cls.cache:
            cls.cache[usability_test.id] = cls(usability_test)
        return cls.cache[usability_test.id]

    def __init__(self, usability_test):
        self.usability_test = usability_test

        obs = Observation.objects.filter(
            step_execution__interaction_step__scenario_task__task__usability_test=usability_test,
            observation_type=time_type,
        )

        versions = sorted(usability_test.versions.all())

        d = defaultdict(lambda: Counter())
        for o in obs:
            scenario_task = o.step_execution.interaction_step.scenario_task
            d[scenario_task.task][scenario_task.scenario.app_version] += o.value
        self.d = d

        self.items = []
        self.stack_names = []
        self.legend_items = [v.name for v in versions]
        # TODO: sort key should be order, but id does not exist
        for task in sorted(d.keys(), key=lambda task: task.name):
            counter = d[task]
            self.stack_names.append(task.name)
            if len(counter.keys()) == len(versions):
                self.items.append({
                    'name': task.name,
                    'values': [counter[app_version] for app_version in versions],
                })

    def get_title(self):
        return self.usability_test.name

    def get_stack_names(self):
        return self.stack_names

    def get_items(self):
        return self.items

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

    def get_items(self):
        all_objs = TaskScenarioExecution.objects.all()
        return all_objs.filter(scenario_execution__participant=self.participant)
