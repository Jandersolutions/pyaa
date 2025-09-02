from django.views.generic import DetailView

from apps.blog.models import Post


class PostDetailView(DetailView):
    """View to display a single blog post."""

    model = Post
    template_name = "pages/blog/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = self.get_object().as_meta(self.request)
        return context
