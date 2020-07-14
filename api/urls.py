from django.urls import path

from .views import DestinationsAPIView

urlpatterns = [
    path('destinations', DestinationsAPIView.as_view()),
]