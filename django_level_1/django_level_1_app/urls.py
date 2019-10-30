from django.conf.urls import url
from django_level_1_app import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]