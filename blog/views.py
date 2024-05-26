from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from pytils.translit import slugify

from blog.models import BlogView


class BlogListView(ListView):
    """Класс для вывода главной страницы раздела - блог."""

    model = BlogView

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """Класс для вывода детальной информации о статье."""

    model = BlogView

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    """Класс для создания карточки со статьей."""

    model = BlogView
    fields = (
        "heading",
        "slug",
        "content",
        "photo",
        "created_at",
        "is_published",
        "views_count",
    )
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """Класс для редактирования карточки со статьей."""

    model = BlogView
    fields = (
        "heading",
        "slug",
        "content",
        "photo",
        "created_at",
        "is_published",
        "views_count",
    )

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:detail", args=[(self.kwargs.get("pk"))])


class BlogDeleteView(DeleteView):
    """Класс для удаления карточки со статьей."""

    model = BlogView
    template_name = "blog/blogview_confirm_delete.html"
    success_url = reverse_lazy("blog:list")
