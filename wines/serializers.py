from rest_framework import serializers 
from wines.models import Bottle, Cork


class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ("id", "name", "cork")


class CorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cork
        fields = ("id", "name", "bottle")