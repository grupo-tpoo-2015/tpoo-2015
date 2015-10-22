# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from usability_tests_executions.models import TaskScenarioExecution
from tasks.models import ObservationType


class Chart(object):

    def as_dict(self):
        return {
            'title': self.get_title(),
            self.get_elements_name(): self.get_elements_as_dict(),
        }

    def get_title(self):
        raise NotImplementedError()

    def get_elements_as_dict(self):
        raise NotImplementedError()


class BarChart(Chart):

    def get_elements_name(self):
        return 'bars'

    def get_elements_as_dict(self):
        return [self.element_as_dict(e) for e in self.get_elements()]

    def get_elements(self):
        raise NotImplementedError()

    def element_as_dict(self):
        raise NotImplementedError()


class StackedBarChart(Chart):
    """
    serviría para contrastar, para cada tarea,
    la performance promedio de los usuarios en distintas versiones de la aplicación
    """

    def get_elements_name(self):
        return 'stacks'

    def get_title(self):
        return "Gráfico de barras apiladas"

    def get_elements_as_dict(self):
        return [self.element_as_dict(e) for e in self.get_elements()]

    def get_elements(self):
        return [
            [
                {
                    'name': "Foo",
                    'value': 23,
                },
                {
                    'name': "Bar",
                    'value': 12,
                },
                {
                    'name': "Baz",
                    'value': 45,
                },
            ],
            [
                {
                    'name': "Foo",
                    'value': 23,
                },
                {
                    'name': "Bar",
                    'value': 12,
                },
                {
                    'name': "Baz",
                    'value': 45,
                },
            ],
            [
                {
                    'name': "Foo",
                    'value': 87,
                },
                {
                    'name': "Bar",
                    'value': 67,
                },
                {
                    'name': "Baz",
                    'value': 145,
                },
            ],
            [
                {
                    'name': "Foo",
                    'value': 223,
                },
                {
                    'name': "Bar",
                    'value': 12,
                },
            ],
            [
                {
                    'name': "Foo",
                    'value': 23,
                },
            ]
        ]

    def element_as_dict(self, stack):
        return stack


class UserTimesPerParticipantBarChart(BarChart):

    def __init__(self, participant):
        self.participant = participant
        self.time_type = ObservationType.objects.get(name='time')

    def get_title(self):
        return 'Tareas realizadas por el participante %s' % self.participant.name

    def element_as_dict(self, scenario_task_execution):
        total = 0
        for step in scenario_task_execution.steps.all():
            if not step.interaction_step.is_question:
                for observation in step.observations.filter(observation_type=self.time_type):
                    total += observation.value

        return {
            'value': total,
            'name': scenario_task_execution.scenario_task.task.name,
        }

    def get_elements(self):
        all_objs = TaskScenarioExecution.objects.all()
        return all_objs.filter(scenario_execution__participant=self.participant)
