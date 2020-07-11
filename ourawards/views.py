from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#User Signup
def signup(request):
    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form })


