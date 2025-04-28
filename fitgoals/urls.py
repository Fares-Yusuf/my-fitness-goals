from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name='landing'),  # landing page = landing
    path('signup/', views.signup, name='signup'),       # Signup page
]
