from django.contrib import admin
from .models import Developer,Project,skill

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','age']
    search_fields = ['first_name','last_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    filter_horizontal = ('developer',)


@admin.register(skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title','developer']
    search_fields = ['title','developer__first_name', 'developer__last_name']