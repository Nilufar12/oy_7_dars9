from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CourseForm, StudentForm
from .models import Course, Student


def home(request: HttpRequest):
    courses = Course.objects.all()
    students = Student.objects.all()

    context = {
        'courses': courses,
        'students': students
    }

    return render(request, 'main/index.html', context)


@permission_required('myproject.view_course', raise_exception=True, login_url='login')
def course_detail(request, course_id: int):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.filter(course=course)

    context = {
        'course': course,
        'student': student
    }

    return render(request, 'main/detail.html')


@permission_required('myproject.view_student', raise_exception=True, login_url='login')
def student_detail(request, student_id: int):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'main/detail.html', context)


@permission_required('myproject.add_course', raise_exception=True, login_url='login')
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        'form': form
    }
    return render(request, 'main/add_course.html', context)


@permission_required('myproject.add_student', raise_exception=True, login_url='login')
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_student.html', context)


@permission_required('myproject.change_student', raise_exception=True, login_url='login')
def update_student(request: HttpRequest, student_id: int):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect(student_detail, student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'main/update_student.html', {'form': form})