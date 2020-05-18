from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

def hi(request):
    return HttpResponse('Say Hi.')

def say_hi_by_name(request, name):
    return render(request, 'student/hello.html', {'aname': name})

def student_list(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, 'student/student_list.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Validation success')
            return redirect('/student_list')
    else:
        form = StudentForm()

    context = {
        "form": form
    }
    return render(request, 'student/add_student.html', context)


def update_student(request, id):
    astudent = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=astudent)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/student_list')
    else:
        form = StudentForm(instance=astudent)

    context = {
        "form": form
    }
    return render(request, 'student/add_student.html', context)


def delete_student(request, id):
    if Student.objects.get(id=id):
        Student.objects.get(id=id).delete()
    else:
        print('student ID not found')

    return redirect('/student_list')




