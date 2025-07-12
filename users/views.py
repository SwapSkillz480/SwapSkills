from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.db.models import Q
from swaps.models import SwapRequest

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    received_swaps = SwapRequest.objects.filter(to_user=request.user).order_by('-created_at')[:5]
    sent_swaps = SwapRequest.objects.filter(from_user=request.user).order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {
        'received_swaps': received_swaps,
        'sent_swaps': sent_swaps,
    })

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})

@login_required
def search_skills(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Profile.objects.filter(
            Q(skills_offered__icontains=query),
            is_public=True
        ).select_related('user')
        # Add a split list of skills to each profile
        for profile in results:
            profile.skills_offered_list = [s.strip() for s in profile.skills_offered.split(',') if s.strip()]
    # Add a split list of skills for the current user
    user_skills_offered_list = []
    if hasattr(request.user, 'profile'):
        user_skills_offered_list = [s.strip() for s in request.user.profile.skills_offered.split(',') if s.strip()]
    return render(request, 'search_results.html', {
        'results': results,
        'query': query,
        'user_skills_offered_list': user_skills_offered_list,
    })
