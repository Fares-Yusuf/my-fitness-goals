from django import forms
from .models import Workouts, Goal

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workouts # fixed spelling mistake
        fields = ['goal', 'date', 'activity_type', 'duration', 'sets', 'reps', 'weight', 'notes']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target', 'is_completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'is_completed': forms.CheckboxInput(),
        }
