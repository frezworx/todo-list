import json

from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from core.forms import TaskForm, TagForm
from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "pages/index.html"
    context_object_name = "tasks"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_create.html"
    success_url = reverse_lazy("core:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_create.html"
    success_url = reverse_lazy("core:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "pages/task_confirm_delete.html"
    success_url = reverse_lazy("core:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "pages/tags.html"
    context_object_name = "tags"
    paginate_by = 10


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "pages/tag_create.html"
    success_url = reverse_lazy("core:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "pages/tag_create.html"
    success_url = reverse_lazy("core:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "pages/tag_confirm_delete.html"
    success_url = reverse_lazy("core:tags-list")


class ToggleTaskStatusView(generic.View):

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.done = not task.done
        task.save()
        page = request.POST.get("page", 1)
        return redirect(f"{reverse('core:task-list')}?page={page}")
