from django.urls import path
from myproject.core.views import index, userprofile_json

app_name = 'core'

urlpatterns = [
            path('', index, name='index'),
            path('json/', userprofile_json, name='userprofile_json'),
            ]

