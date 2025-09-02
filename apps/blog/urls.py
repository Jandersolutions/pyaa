from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path(
        "posts/",
        views.PostListAPIView.as_view(),
        name="post-list",
    ),
    path(
        "posts/<slug:slug>/",
        views.PostRetrieveAPIView.as_view(),
        name="post-detail",
    ),
]
