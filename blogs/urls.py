from django.urls import path

from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name = 'blog_detail')
]