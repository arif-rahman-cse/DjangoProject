from rest_framework import serializers

from test_app.models import Destination

class DestinationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'