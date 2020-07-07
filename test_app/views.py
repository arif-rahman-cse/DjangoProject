from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Dhaka'
    dest1.desc = 'Dhaka (or Dacca) is the capital and largest city of Bangladesh. It is the cultural and economic hub of the country. Having a colossal historical background, the old part of the city, known as Old Dhaka or Old Town'
    dest1.img = 'destination_1.jpg'
    dest1.price = '800'
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Chattogram'
    dest2.desc = 'Chittagong is large port city on the southeastern coast of Bangladesh. The Ethnological Museum has exhibits about the many different ethnic tribes across the country.'
    dest2.img = 'destination_2.jpg'
    dest2.price = '900'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Mymensingh'
    dest3.desc = 'Mymensingh is the capital of Mymensingh Division of Bangladesh. The city is located on the Brahmaputra River, about 120 km north of Dhaka the capital of the country'
    dest3.img = 'destination_3.jpg'
    dest3.price = '800'
    dest3.offer = True

    dests = [dest1, dest2, dest3 ]

    return render(request, 'index.html', {'destinations': dests})

def showDetails(request):
    userName = request.POST['username']
    return render(request, 'welcome_page.html', {'email': userName})