from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Task

# Create your views here.

class Home(TemplateView):
    template_name='task/index.html'


class TaskListView(ListView):
    model=Task

class TaskDetailView(DetailView):
    model=Task

class TaskCreateView(CreateView):
    model=Task
    fields=['notes','date_created']
    success_url='/'   


class TaskUpdateView(UpdateView):
    model=Task
    fields=['notes','date_created']
    success_url='/'   


class TaskDeleteView(DeleteView):
    model=Task
    success_url='/' 


