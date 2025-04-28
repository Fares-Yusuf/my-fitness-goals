from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['goal', 'date', 'activity_type', 'duration', 'sets', 'reps', 'weight', 'notes']
