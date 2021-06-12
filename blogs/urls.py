from django.urls import path

from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name = 'blog_detail'),
    path('blog/new', views.BlogCreateView.as_view(), name='new_blog'),
    path('blog/<int:pk>/edit', views.BlogUpdateView.as_view(), name = 'update_blog'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete')
]