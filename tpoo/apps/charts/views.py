from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from usability_tests.models import UsabilityTest
from usability_tests_executions.models import Participant
from .charts import ParticipantTimesPerTaskBarChart, CompareTaskBetweenVersionsChart, UsabilityTestTreeChart


def usability_test_view(some_view):

    def wrapper(request, usability_test_id, **kwargs):
        usability_test = get_object_or_404(UsabilityTest, id=usability_test_id)
        request.usability_test = usability_test
        template_name, context = some_view(request, usability_test, **kwargs)
        context['current_usability_test'] = usability_test
        return render(request, template_name, context)

    return wrapper


@login_required
@usability_test_view
def tree_chart(request, usability_test):

    return 'charts/tree.jinja', {
        'tree_data': UsabilityTestTreeChart(usability_test).as_dict(),
        'tree_chart_is_active': True,
    }


@login_required
@usability_test_view
def bar_charts(request, usability_test):

    return 'charts/bar_charts.jinja', {
        'participants': Participant.objects.all(),
        'bar_charts_is_active': True,
    }


@login_required
@usability_test_view
def bar_chart(request, usability_test,  participant_id):

    participant = get_object_or_404(Participant, id=participant_id)

    return 'charts/bar_chart.jinja', {
        'dataset': ParticipantTimesPerTaskBarChart(participant).as_dict(),
        'bar_charts_is_active': True,
    }


@login_required
@usability_test_view
def stacked_bar_chart(request, usability_test):

    dataset = CompareTaskBetweenVersionsChart(usability_test).as_dict()

    return 'charts/stacked_bar_chart.jinja', {
        'dataset': dataset,
        'stacked_bar_chart_is_active': True,
    }
