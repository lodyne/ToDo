from django.urls import path
from . import views
from .views import(
    Home,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView

) 


urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('task/',TaskListView.as_view(),name='task-list'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('task/new',TaskCreateView.as_view(),name='task-create'),
    path('task/<int:pk>/edit/',TaskUpdateView.as_view(),name='task-update'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='task-delete')

]