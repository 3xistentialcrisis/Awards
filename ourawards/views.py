from django.shortcuts import render, redirect
from .forms import SignupForm
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
#Index Page
def index(request):
    return render(request, 'index.html')

#Profile View
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    print(queryset)
    serializer_class = ProfileSerializer

#User View
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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


