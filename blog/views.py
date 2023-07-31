from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'



class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs')


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object



class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')