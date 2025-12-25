from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import Developer, Project, Skill
from .forms import DeveloperForm, ProjectForm, SkillForm
from django.contrib.auth.mixins import LoginRequiredMixin

SkillFormSet = inlineformset_factory(Developer, Skill, form=SkillForm, extra=1, can_delete=True)

# Developer Views
class DeveloperListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = 'skilldev/developer_list.html'
    context_object_name = 'developers'

    def get_queryset(self):
        return Developer.objects.prefetch_related('projects', 'skills').all()

class DeveloperDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Developer
    template_name = 'skilldev/developer_detail.html'
    context_object_name = 'developer'

class DeveloperCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Developer
    form_class = DeveloperForm
    template_name = 'skilldev/developer_form.html'
    success_url = reverse_lazy('developer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['skill_formset'] = SkillFormSet(self.request.POST)
        else:
            context['skill_formset'] = SkillFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        skill_formset = context['skill_formset']
        if skill_formset.is_valid():
            self.object = form.save()  # اول Developer ذخیره می‌شود
            skill_formset.instance = self.object
            skill_formset.save()       # سپس Skillها ذخیره می‌شوند
            messages.success(self.request, "Developer created successfully.")
            return super().form_valid(form)
        else:
            return self.form_invalid(form)



class DeveloperUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = Developer
    form_class = DeveloperForm
    template_name = 'skilldev/developer_form.html'
    success_url = reverse_lazy('developer_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['skill_formset'] = SkillFormSet(self.request.POST, instance=self.object)
        else:
            data['skill_formset'] = SkillFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        skill_formset = context['skill_formset']
        if form.is_valid() and skill_formset.is_valid():
            self.object = form.save()
            skill_formset.instance = self.object
            skill_formset.save()
            messages.success(self.request, "Developer updated successfully.")
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class DeveloperDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Developer
    template_name = 'skilldev/developer_confirm_delete.html'
    success_url = reverse_lazy('developer_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Developer deleted.")
        return super().delete(request, *args, **kwargs)


# Project Views
class ProjectListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Project
    template_name = 'skilldev/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('developers').all()

class ProjectDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Project
    template_name = 'skilldev/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Project
    form_class = ProjectForm
    template_name = 'skilldev/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Project created successfully.")
        return response

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = Project
    form_class = ProjectForm
    template_name = 'skilldev/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()  # ذخیره خود پروژه
        form.save_m2m()  # ذخیره روابط ManyToMany
        messages.success(self.request, "Project updated successfully.")
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Project
    template_name = 'skilldev/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Project deleted.")
        return super().delete(request, *args, **kwargs)