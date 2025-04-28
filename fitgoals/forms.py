from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['goal', 'date', 'activity_type', 'duration', 'sets', 'reps', 'weight', 'notes']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target', 'is_completed']