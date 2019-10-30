from django.conf.urls import url
from django_level_5_app import views


# Template URLS
app_name = 'django_level_5_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
