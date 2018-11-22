from django.shortcuts import render
from django.views.generic import ListView
from core.models import Jobadd

class JobaddList(ListView):
    model = Jobadd
