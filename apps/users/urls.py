from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.jinja'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^register/$', 'users.views.register', name='register'),
]
