from django.urls import path

from . import views

app_name = "blog_admin"

urlpatterns = [
    path(
        "comments/<int:pk>/approve/",
        views.CommentApproveAPIView.as_view(),
        name="comment-approve",
    ),
    path(
        "comments/<int:pk>/delete/",
        views.CommentDeleteAPIView.as_view(),
        name="comment-delete",
    ),
]
