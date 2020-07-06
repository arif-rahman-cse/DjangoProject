from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def showDetails(request):
    userName = request.POST['username']
    return render(request, 'welcome_page.html', {'email': userName})