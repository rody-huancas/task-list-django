from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import home, TaskList, TaskCreate, TaskUpdate

urlpatterns = [
    path("", home, name="home"),
    path("tasks/", TaskList.as_view(), name="tasks"),
    path("task/create/", TaskCreate.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
]
