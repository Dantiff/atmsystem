# banking/urls.py
from django.conf.urls import url
from banking import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^about/$', views.about_page),
    url(r'^login/$', views.login_page),
    url(r'^accounts/login/$', views.login_page),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register_page),
]