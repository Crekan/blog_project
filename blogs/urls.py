from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
