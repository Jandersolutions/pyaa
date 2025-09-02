from django.views.generic import DetailView, ListView

from apps.blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "pages/blog/list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(is_published=True).order_by("-created_at")
    paginate_by = 10


class PostDetailView(DetailView):
    """View to display a single blog post."""

    model = Post
    template_name = "pages/blog/detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = self.get_object().as_meta(self.request)
        return context
