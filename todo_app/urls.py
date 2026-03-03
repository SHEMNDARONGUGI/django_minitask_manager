from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.tasks_page, name="tasks"),
    path('update/<int:id>/', views.update_task, name="update_task"),
    path('delete/<int:id>/', views.delete_task, name="delete_task")
]
