import random
from django.shortcuts import render


def test(request):

    amount = random.randint(10, 15)
    dataset = {
        'title': 'Tareas realizadas por el participante Juan Carlos Batman',
        'elements': [{
            'name': "Tarea #%d" % i,
            'time': random.uniform(10, 100),
        } for i in xrange(amount)]
    }

    return render(request, 'charts/prueba.jinja', {
        'dataset': dataset,
    })
