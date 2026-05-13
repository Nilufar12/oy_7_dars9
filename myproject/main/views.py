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


def course_detail(request, course_id: int):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.filter(course=course)

    context = {
        'course': course,
        'student': student
    }

    return render(request, 'main/detail.html')


def student_detail(request, student_id: int):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }

    return render(request, 'main/detail.html', context)


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