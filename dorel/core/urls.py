from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('jobadds', views.JobaddList.as_view(), name='JobaddList'),
]