from django.conf.urls import url

urlpatterns = [

    url(r'^bar_chart/(?P<participant_id>\d+)$',
        'charts.views.bar_chart',
        name='bar_chart'),
]
