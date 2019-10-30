from django.conf.urls import url
from django_level_4_app import views


# Template Tagging
app_name = 'django_level_4_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
