from django.urls import reverse_lazy
from django.views import generic

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
    pass


class TaskDeleteView(generic.DeleteView):
    pass


class TaskToggleView(generic.View):
    pass


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
    pass


class TagsDeleteView(generic.DeleteView):
    pass
