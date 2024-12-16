from django.urls import path

from core.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleView,
    TagListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

app_name = "core"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view, name="task-delete"),
    path("task/<int:pk>/toggle", TaskToggleView.as_view, name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>update", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]
