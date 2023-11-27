from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Api', views.ApiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
