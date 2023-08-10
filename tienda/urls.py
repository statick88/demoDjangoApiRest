from django.urls import include, path
from rest_framework import routers
from .views import TiendaViewSet

router = routers.DefaultRouter()
router.register(r'tiendas', TiendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
