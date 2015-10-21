from usability_tests_executions.models import TaskScenarioExecution
from tasks.models import ObservationType


class Chart(object):

    def as_dict(self):
        return {
            'title': self.get_title(),
            'bars': self.get_bars_as_dict(),
        }

    def get_title(self):
        raise NotImplementedError()

    def get_bars_as_dict(self):
        raise NotImplementedError()


class BarChart(Chart):

    def get_bars_as_dict(self):
        return [self.bar_as_dict(e) for e in self.get_bars()]

    def get_bars(self):
        raise NotImplementedError()

    def bar_as_dict(self):
        raise NotImplementedError()


class StackedBarChart(Chart):

    def get_bars_as_dict(self):
        return [[self.bar_as_dict(e)] for e in self.get_bars()]

    def get_bars(self):
        raise NotImplementedError()

    def bar_as_dict(self):
        raise NotImplementedError()


class UserTimesPerParticipantBarChart(BarChart):

    def __init__(self, participant):
        self.participant = participant
        self.time_type = ObservationType.objects.get(name='time')

    def get_title(self):
        return 'Tareas realizadas por el participante %s' % self.participant.name

    def bar_as_dict(self, scenario_task_execution):
        total = 0
        for step in scenario_task_execution.steps.all():
            if not step.interaction_step.is_question:
                for observation in step.observations.filter(observation_type=self.time_type):
                    total += observation.value

        return {
            'value': total,
            'name': scenario_task_execution.scenario_task.task.name,
        }

    def get_bars(self):
        all_objs = TaskScenarioExecution.objects.all()
        return all_objs.filter(scenario_execution__participant=self.participant)
