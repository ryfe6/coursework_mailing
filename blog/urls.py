from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                        BlogListView, BlogUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path("list", cache_page(60)(BlogListView.as_view()), name="list"),
    path("create", BlogCreateView.as_view(), name="create"),
    path("update/<int:pk>", BlogUpdateView.as_view(), name="update"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
]
