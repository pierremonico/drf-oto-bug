from rest_framework.routers import DefaultRouter

from wines.views import BottleViewSet, CorkViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bottles', BottleViewSet)
router.register(r'corks', CorkViewSet)
