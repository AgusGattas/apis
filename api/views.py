from rest_framework import viewsets
from .serializer import ApiSerializer
from .models import Api

# Create your views here.


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
