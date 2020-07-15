from django.urls import path

from .views import DestinationsAPIView
from .views import DestinationsAPIDetailView
from .views import DestinationsAPINewView

urlpatterns = [
    path('destinations', DestinationsAPIView.as_view()),
    path('destinations/<int:pk>/', DestinationsAPIDetailView.as_view()),
    path('destinations/new', DestinationsAPINewView.as_view()),
]