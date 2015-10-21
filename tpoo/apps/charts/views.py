from django.shortcuts import render, get_object_or_404
from usability_tests_executions.models import Participant
from .models import UserTimesPerParticipantBarChart, StackedBarChart


def home(request):
    return render(request, 'charts/home.jinja', {
        'participants': Participant.objects.all(),
    })


def bar_chart(request, participant_id):

    participant = get_object_or_404(Participant, id=participant_id)

    return render(request, 'charts/bar_chart.jinja', {
        'dataset': UserTimesPerParticipantBarChart(participant).as_dict(),
    })


def stacked_bar_chart(request):

    return render(request, 'charts/stacked_bar_chart.jinja', {
        'dataset': StackedBarChart().as_dict(),
    })
