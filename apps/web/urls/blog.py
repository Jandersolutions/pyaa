from django.urls import path

from ..views import blog as views

app_name = "web"

urlpatterns = [
    path(
        "blog/<slug:slug>/",
        views.PostDetailView.as_view(),
        name="blog_detail",
    ),
]
