from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Blog
# Create your views here.
class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'new_blog.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'update_blog.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')