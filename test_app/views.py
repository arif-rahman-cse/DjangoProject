from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):

    # Fatching Data from Database 
    dests = Destination.objects.all()

    return render(request, 'index.html', {'destinations': dests})

def showDetails(request):
    userName = request.POST['username']
    return render(request, 'welcome_page.html', {'email': userName})