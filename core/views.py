from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "pages/index.html"
    context_object_name = "tasks"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    pass


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
    paginate_by = 5


class TagsCreateView(generic.CreateView):
    pass


class TagsUpdateView(generic.UpdateView):
    pass


class TagsDeleteView(generic.DeleteView):
    pass
