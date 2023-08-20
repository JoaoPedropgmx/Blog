from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='home'),
    path('postagem/<int:pk>/', views.post_detalhes, name='post_detalhes')
]