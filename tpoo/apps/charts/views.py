import random
from django.shortcuts import render, get_object_or_404
from usability_tests.models import UsabilityTest
from usability_tests_executions.models import Participant
from .models import ParticipantTimesPerTaskBarChart, CompareTaskBetweenVersionsChart


def home(request):
    return render(request, 'charts/home.jinja', {
        'participants': Participant.objects.all(),
        'usability_tests': UsabilityTest.objects.all(),
    })


def bar_chart(request, participant_id):

    participant = get_object_or_404(Participant, id=participant_id)

    return render(request, 'charts/bar_chart.jinja', {
        'dataset': ParticipantTimesPerTaskBarChart(participant).as_dict(),
    })


def stacked_bar_chart(request, usability_test_id):

    usability_test = get_object_or_404(UsabilityTest, id=usability_test_id)

    return render(request, 'charts/stacked_bar_chart.jinja', {
        'dataset': CompareTaskBetweenVersionsChart.get(usability_test).as_dict(),
    })
