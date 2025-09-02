from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path(
        "posts/",
        views.PostListCreateAPIView.as_view(),
        name="post-list",
    ),
    path(
        "posts/<slug:slug>/",
        views.PostRetrieveUpdateDestroyAPIView.as_view(),
        name="post-detail",
    ),
    path(
        "posts/<slug:slug>/comments/",
        views.CommentListCreateAPIView.as_view(),
        name="comment-list-create",
    ),
]
