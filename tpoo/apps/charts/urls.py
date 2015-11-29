from django.conf.urls import url

urlpatterns = [

    url(r'^(?P<usability_test_id>\d+)/tree/$',
        'charts.views.tree_chart',
        name='tree_chart'),

    url(r'^(?P<usability_test_id>\d+)/stacked-bar-chart/$',
        'charts.views.stacked_bar_chart',
        name='stacked_bar_chart'),

    url(r'^(?P<usability_test_id>\d+)/bar-charts/$',
        'charts.views.bar_charts',
        name='bar_charts'),

    url(r'^(?P<usability_test_id>\d+)/bar-charts/(?P<participant_id>\d+)$',
        'charts.views.bar_chart',
        name='bar_chart'),

]
