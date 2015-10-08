from usability_tests_executions.models import TaskScenarioExecution
from tasks.models import ObservationType


class Chart(object):

    def as_dict(self):
        return {
            'title': self.get_title(),
            'elements': self.get_elements_as_dict(),
        }

    def get_elements_as_dict(self):
        raise NotImplementedError()


class BarChart(Chart):

    def get_title(self):
        raise NotImplementedError()

    def get_elements_as_dict(self):
        return [self.element_as_dict(e) for e in self.get_elements()]

    def get_elements(self):
        raise NotImplementedError()

    def element_as_dict(self):
        raise NotImplementedError()


class UserTimesPerParticipantBarChart(BarChart):

    def __init__(self, participant):
        self.participant = participant
        self.time_type = ObservationType.objects.get(name='time')

    def get_title(self):
        return 'Tareas realizadas por el participante %s' % self.participant.name

    def element_as_dict(self, scenario_task_execution):
        total = 0
        for step in scenario_task_execution.steps.all():
            for observation in step.observations.filter(observation_type=self.time_type):
                total += observation.value

        return {
            'time': total,
            'name': scenario_task_execution.scenario_task.task.name,
        }

    def get_elements(self):
        all_objs = TaskScenarioExecution.objects.all()
        return all_objs.filter(scenario_execution__participant=self.participant)
