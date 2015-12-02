from django.conf.urls import url
from .views import (
    TreeChartView,
    StackedBarChartView,
    BarChartsView,
    BarChartView,
)

urlpatterns = [

    url(r'^(?P<usability_test_id>\d+)/tree/$',
        TreeChartView.as_view(),
        name='tree_chart'),

    url(r'^(?P<usability_test_id>\d+)/stacked-bar-chart/$',
        StackedBarChartView.as_view(),
        name='stacked_bar_chart'),

    url(r'^(?P<usability_test_id>\d+)/bar-charts/$',
        BarChartsView.as_view(),
        name='bar_charts'),

    url(r'^(?P<usability_test_id>\d+)/bar-chart/(?P<participant_id>\d+)$',
        BarChartView.as_view(),
        name='bar_chart'),

]
