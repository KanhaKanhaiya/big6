"""File to put views"""

from django.shortcuts import render

# Create your views here.

def homePage(request):
    data = {"title":"The big6 Project", "body":"Welcome to The big6 Project"}
    return render(request, "index.html", data)
