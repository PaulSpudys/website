from django.urls import path
from . import views
from project.views import contact, success


urlpatterns = [
    path('', views.project, name='projects' ),
    path('single-projects/<str:pk>/', views.projects, name="project" ),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('contact/', contact, name='contact'),
    path('success.html', success, name='success')
]
    



