from django.views import generic

from core.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "index.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    pass


class TaskUpdateView(generic.UpdateView):
    pass


class TaskDeleteView(generic.DeleteView):
    pass


class TaskToggleView(generic.View):
    pass


class TagListView(generic.ListView):
    pass


class TagsCreateView(generic.CreateView):
    pass


class TagsUpdateView(generic.UpdateView):
    pass


class TagsDeleteView(generic.DeleteView):
    pass
