from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  .models import Task

# Create your views here.

class TaskList(ListView):
    context_object_name = 'tasks'
    model = Task

class TaskDetail(DetailView):
    model = Task
