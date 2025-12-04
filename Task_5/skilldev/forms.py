from django import forms
from django.core.exceptions import ValidationError
from .models import Developer, Project, Skill

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'email', 'age']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            return age
        if age < 18:
            raise ValidationError("سن باید حداقل 18 سال باشد.")
        return age

class ProjectForm(forms.ModelForm):
    developers = forms.ModelMultipleChoiceField(
        queryset=Developer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'developers']

    def clean(self):
        cleaned = super().clean()
        desc = cleaned.get('description') or ''
        if desc.strip() == '':
            raise ValidationError("توضیحات پروژه نباید خالی باشد.")
        return cleaned

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'description']