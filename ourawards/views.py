from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#User Signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form })

#Profile
def profile(request, username):
    return render(request, 'profile.html')


