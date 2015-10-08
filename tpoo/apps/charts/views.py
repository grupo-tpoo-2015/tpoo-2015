from django.shortcuts import render
from usability_tests_executions.models import Participant
from .models import UserTimesPerParticipantBarChart


def test(request):

    participant = Participant.objects.order_by('?').first()  # random participant

    return render(request, 'charts/prueba.jinja', {
        'dataset': UserTimesPerParticipantBarChart(participant).as_dict(),
    })
