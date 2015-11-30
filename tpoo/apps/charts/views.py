from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from usability_tests.models import UsabilityTest
from usability_tests_executions.models import Participant
from .charts import (
    ParticipantTimesPerTaskBarChart,
    CompareTaskBetweenVersionsChart,
    UsabilityTestTreeChart,
)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class UsabilityTestView(View, LoginRequiredMixin):

    template_name = NotImplemented

    def build_context(self, request, usability_test_id, *args):
        raise NotImplementedError()

    def get(self, request, usability_test_id, *args):
        usability_test = get_object_or_404(UsabilityTest, id=usability_test_id)
        context = self.build_context(request, usability_test, *args)
        context['current_usability_test'] = usability_test
        return render(request, self.template_name, context)


class TreeChartView(UsabilityTestView):

    # template_name = 'charts/horizontal_tree.jinja'
    template_name = 'charts/vertical_tree.jinja'

    def build_context(self, request, usability_test):
        return {
            'tree_data': UsabilityTestTreeChart(usability_test).as_dict(),
            'tree_chart_is_active': True,
        }


class StackedBarChartView(UsabilityTestView):

    template_name = 'charts/stacked_bar_chart.jinja'

    def build_context(self, request, usability_test):
        dataset = CompareTaskBetweenVersionsChart(usability_test).as_dict()
        return {
            'dataset': dataset,
            'stacked_bar_chart_is_active': True,
        }


class BarChartsView(UsabilityTestView):

    template_name = 'charts/bar_charts.jinja'

    def build_context(self, request, usability_test):
        return {
            'participants': Participant.objects.all(),
            'bar_charts_is_active': True,
        }


class BarChartView(UsabilityTestView):

    template_name = 'charts/bar_chart.jinja'

    def build_context(self, request, usability_test,  participant_id):
        participant = get_object_or_404(Participant, id=participant_id)
        return {
            'dataset': ParticipantTimesPerTaskBarChart(participant).as_dict(),
            'bar_charts_is_active': True,
        }
