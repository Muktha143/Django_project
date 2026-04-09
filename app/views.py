from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserData
from .forms import UserForm, AadhaarSearchForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Registration successful! Aadhaar and PAN numbers were generated automatically.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form, 'update': False})

def search(request):
    users = None
    form = AadhaarSearchForm(request.GET or None)
    
    if request.GET:
        if request.GET.get('aadhaar_number'):
            aadhaar = request.GET.get('aadhaar_number')
            users = UserData.objects.filter(aadhaar_number=aadhaar)
        elif request.GET.get('pan_number'):
            pan = request.GET.get('pan_number')
            users = UserData.objects.filter(pan_number=pan)
    
    return render(request, 'search.html', {'form': form, 'users': users})

def user_list(request):
    users = UserData.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_detail(request, pk):
    user = get_object_or_404(UserData, pk=pk)
    return render(request, 'user_detail.html', {'user': user})


def update_user(request, pk):
    user = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully.')
            return redirect('user_detail', pk=user.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm(instance=user)
    return render(request, 'register.html', {'form': form, 'update': True, 'user': user})


def delete_user(request, pk):
    user = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User record deleted successfully.')
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})


def aadhaar_card(request, aadhaar):
    user = get_object_or_404(UserData, aadhaar_number=aadhaar)
    return render(request, 'aadhaar_card.html', {'user': user})

def pan_card(request, pan):
    user = get_object_or_404(UserData, pan_number=pan)
    return render(request, 'pan_card.html', {'user': user})