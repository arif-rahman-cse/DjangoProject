from rest_framework import generics, permissions
from test_app.models import Destination
from .serializers import DestinationSerializer

# Create your views here.

class DestinationsAPIView(generics.ListAPIView):
    #  View  level Permissions
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
 

class DestinationsAPIDetailView(generics.RetrieveUpdateDestroyAPIView): # Get update and delete 
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationsAPINewView(generics.ListCreateAPIView):
    queryset = Destination.objects.all().order_by('-id')[:1] # Desending order and single item 
    serializer_class = DestinationSerializer