from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.http import HttpResponseRedirect


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, "home.html", {"form": form, "candidates": candidates})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")


class CandidateView(View):
    def get(self, request, id):
        candidate = Resume.objects.get(pk=id)
        return render(request, "candidate.html", {"candidate": candidate})
