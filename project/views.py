from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.http import HttpResponse

def project(request):
    return render(request, 'project.html')


def projects(request, pk):
    return HttpResponse('This is our Projects page: '+str(pk))