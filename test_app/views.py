from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html', {'name': 'Django Framwork'})

def showDetails(request):
    userName = request.GET['username']
    return render(request, 'welcome_page.html', {'email': userName})