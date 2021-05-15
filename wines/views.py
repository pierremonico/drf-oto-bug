from rest_framework import viewsets

from wines.models import Bottle, Cork
from wines.serializers import BottleSerializer, CorkSerializer


class BottleViewSet(viewsets.ModelViewSet):
    serializer_class = BottleSerializer
    queryset = Bottle.objects.all()


class CorkViewSet(viewsets.ModelViewSet):
    serializer_class = CorkSerializer
    queryset = Cork.objects.all()