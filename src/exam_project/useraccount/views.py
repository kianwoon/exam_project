#from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            f = CustomUserCreationForm(request.POST)
            if f.is_valid():
                f.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')

        else:
            f = CustomUserCreationForm()


        return render(request, 'register.html', {'form': f})
    else:
        return redirect('home')