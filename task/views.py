from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

class Home(TemplateView):
    template_name='task/home.html'


class TaskListView(ListView):
    model=Task

class TaskDetailView(DetailView):
    model=Task

class TaskCreateView(CreateView):
    model=Task
    fields=['notes','date_created']
    success_url='/task'   


class TaskUpdateView(UpdateView):
    model=Task
    fields=['notes','date_created']
    success_url='/task'   


class TaskDeleteView(DeleteView):
    model=Task
    success_url='/task' 

class APIOverview(APIView):
    def get(self, request, format=None):
        api_urls = {
            'List': 'task_list/',
            'Detail-View': 'task_detail/<int:pk>/',
            'Create':'task_create/new',
            'Edit':'task_edit/<int:pk>/edit/',
            'Delete': 'task_delete/<int:pk>/delete/',
        }
        
        return Response(api_urls)
    
class APITaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class APITaskCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer
    success_url='/api/task_list/' 

class APITaskRetrieve(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class APITaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    success_url='/api/task_list/'

class APITaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    success_url='/api/task_list/'

