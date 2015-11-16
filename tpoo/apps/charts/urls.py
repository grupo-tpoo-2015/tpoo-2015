from django.conf.urls import url

urlpatterns = [

    url(r'^bar_chart/(?P<participant_id>\d+)$',
        'charts.views.bar_chart',
        name='bar_chart'),

    url(r'^stacked_bar_chart/(?P<usability_test_id>\d+)$',
        'charts.views.stacked_bar_chart',
        name='stacked_bar_chart'),
]
