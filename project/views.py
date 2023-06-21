from django.shortcuts import render, redirect
from django.http import HttpResponse
from project.forms import ContactForm
from .models import Project
import csv

# Create your views here.from django.http import HttpResponse


def resume(request):
    resume = Project.objects.all()
    context = {'resume': resume}
    return render(request, 'project/resume.html', context)

def about(request):
    about = Project.objects.all()
    context = {'about': about}
    return render(request, 'project/about.html', context)

def project(request):
    project = Project.objects.all()
    context = {'projects': project}
    return render(request, 'project/project.html', context)


def projects(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project' : projectObj}
    return render(request, 'project/single-projects.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            file = open('responses.csv', 'a')
            writer = csv.writer(file)
            writer.writerow([name,email,message])
            file.close()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'project/contact.html', {'form': form})


def success(request):
   return render(request, 'project/success.html', {'success':success} )





