from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from usability_tests.models import UsabilityTest
from usability_tests_executions.models import Participant
from .charts import ParticipantTimesPerTaskBarChart, CompareTaskBetweenVersionsChart, UsabilityTestTreeChart


@login_required
def home(request):

    datasets = []
    for usability_test in UsabilityTest.objects.all():
        datasets.append(CompareTaskBetweenVersionsChart.get(usability_test).as_dict())

    return render(request, 'charts/home.jinja', {
        'datasets': datasets,
        'participants': Participant.objects.all(),
        'usability_tests': UsabilityTest.objects.all(),
        'charts_active': True,
        'tree_data': UsabilityTestTreeChart(UsabilityTest.objects.first()).as_dict(),
    })


@login_required
def bar_chart(request, participant_id):

    participant = get_object_or_404(Participant, id=participant_id)

    return render(request, 'charts/bar_chart.jinja', {
        'dataset': ParticipantTimesPerTaskBarChart(participant).as_dict(),
        'charts_active': True,
    })
