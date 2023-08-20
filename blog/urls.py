from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='home'),
    path('postagem/<int:pk>/', views.post_detalhes, name='post_detalhes'),
    path('postagem/new/', views.post_news, name='post_new'),
    path('postagem/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('postagem/<int:pk>/delete/', views.post_delete, name='post_delete')
]