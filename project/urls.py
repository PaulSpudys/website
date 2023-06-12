from django.urls import path
from . import views


urlpatterns = [
    path('', views.project ),
    path('projects/<str:pk>/', views.projects )
]
