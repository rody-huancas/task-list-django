from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task


def home(request):
    return render(request, "home.html")


class TaskList(ListView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La tarea fue creada correctamente.")
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        messages.success(self.request, "La tarea fue actualizada correctamente.")
        return super(TaskUpdate, self).form_valid(form)
