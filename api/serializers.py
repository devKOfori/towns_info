from rest_framework import serializers
from .models import Region, District, Town

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ["name"]