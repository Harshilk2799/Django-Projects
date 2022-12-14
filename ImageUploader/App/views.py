from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponseRedirect
from .models import Image

# This function normally use to upload image
def home(request):
    if request.method == "POST":
        print(request.FILES["photo"])
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ImageForm()
    images = Image.objects.all()
    return render(request, "home.html", {"form": form, "images": images})
