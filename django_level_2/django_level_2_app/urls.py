from django.conf.urls import url
from django_level_2_app import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]
