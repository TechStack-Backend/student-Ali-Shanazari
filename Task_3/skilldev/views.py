from django.shortcuts import render, redirect, get_object_or_404
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm

def developer_list(request):
    developers = Developer.objects.prefetch_related('projects','skills').all()
    return render(request, 'skilldev/developer_list.html', {'developers':developers})

def developer_create(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('developer_list')
    else:
        form = DeveloperForm()
    return render(request, 'skilldev/developer_form.html', {'form':form})

def project_list(request):
    projects = Project.objects.prefetch_related('developer').all()
    return render(request, 'skilldev/project_list.html', {'projects':projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'skilldev/project_form.html', {'form':form})




