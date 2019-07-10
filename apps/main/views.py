from django.shortcuts import render, redirect
from .models import Profile
# Create your views here.
def index(request):
    return render(request, "main/index.html", {"users": Profile.objects.all()})

def create(request):

    Profile.objects.create(username=request.POST["username"],pic=request.FILES["pic"])
    return redirect("/")

