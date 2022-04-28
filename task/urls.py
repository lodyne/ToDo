from django.urls import path
from . import views
from .views import(
    Home,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
)

from .views import(
    APIOverview,
    APITaskList,
    APITaskCreate,
    APITaskRetrieve,
    APITaskDelete,
    APITaskUpdate,
    
)

urlpatterns =[
    path('',Home.as_view(),name='home'),

    # * urls for django rest framework

    path('api/',APIOverview.as_view(),name='api'),
    path('api/task_list/',APITaskList.as_view(),name='api-list'),
    path('api/task_create/new',APITaskCreate.as_view(),name='api-create'),
    path('api/task_detail/<int:pk>/',APITaskRetrieve.as_view(),name='api-detail'),
    path('api/task_edit/<int:pk>/edit/',APITaskUpdate.as_view(),name='api-update'),
    path('api/task_delete/<int:pk>/delete/',APITaskDelete.as_view(),name='api-delete'),

    # * urls for traditional django
    
    path('task/',TaskListView.as_view(),name='task-list'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('task/new',TaskCreateView.as_view(),name='task-create'),
    path('task/<int:pk>/edit/',TaskUpdateView.as_view(),name='task-update'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='task-delete')

]