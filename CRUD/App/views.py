from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

# This Function will Add New Student and Show All Student Information
def add_show_student(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            em = form.cleaned_data["email"]
            pw = form.cleaned_data["password"]
            user = User(name=nm, email=em, password=pw)
            user.save()
            return HttpResponseRedirect("/")
    else:
        form = StudentRegistration()
    students = User.objects.all()
    return render(request, "addandshow.html", {"form": form, "students": students})


# This Function will delete student
def delete_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


# This Function will Update Student Information
def update_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request, "updateStudent.html", {"form": form})
