from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import GoalForm
from .models import Goal

class Landing(LoginView):
    template_name = 'landing.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('dashboard')  # Redirect to dashboard after signup
        else:
            error_message = 'Invalid sign up - please try again.'
    else:
        form = UserCreationForm()
        error_message = ''
    
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/list.html', {'goals': goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/goals.html', {'form': form, 'action': 'Add Goal'})
