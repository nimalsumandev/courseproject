from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Course

def home(request):
    return render(request, 'courses/home.html')

# TASK 8a: User Registration
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'courses/signup.html', {'form': form})

# TASK 8b & 8d: User Login & Error Handling
def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('course_list')
        else:
            error_message = "Invalid username or password."
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form, 'error_message': error_message})

# TASK 9a: Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# TASK 5 & 9c: View Courses (Protected)
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# TASK 4 & 9b: Add Course (Protected)
@login_required
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        
        Course.objects.create(
            course_name=course_name,
            course_code=course_code,
            duration=duration,
            fee=fee
        )
        return redirect('course_list')
    return render(request, 'courses/add_course.html')

# TASK 6 & 9b: Edit Course (Protected)
@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.course_name = request.POST.get('course_name')
        course.course_code = request.POST.get('course_code')
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        course.save()
        return redirect('course_list')
    return render(request, 'courses/edit_course.html', {'course': course})

# TASK 7 & 9b: Delete Course (Protected)
@login_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')
