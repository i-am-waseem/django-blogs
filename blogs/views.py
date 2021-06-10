from django.views.generic import ListView, DetailView

from .models import Blog
# Create your views here.
class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'