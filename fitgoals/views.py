from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

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
