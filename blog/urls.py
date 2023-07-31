from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)