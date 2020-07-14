from rest_framework import generics
from test_app.models import Destination
from .serializers import DestinationSerializer

# Create your views here.

class DestinationsAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
