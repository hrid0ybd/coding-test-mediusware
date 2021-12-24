# APP URL
from django.urls import include, re_path
from base import views


urlpatterns = [
    re_path(r'', views.index),
    re_path(r'^home$', views.index),
    re_path(r'^navigation$', views.index)
]
