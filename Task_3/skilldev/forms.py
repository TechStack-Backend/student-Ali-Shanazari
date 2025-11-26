from django import forms
from .models import Project,Developer

class ProjectForm(forms.ModelForm):
    developer = forms.ModelMultipleChoiceField(
        queryset=Developer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = ['title','description','developer']

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name','last_name','email','age']