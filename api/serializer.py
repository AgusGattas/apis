from rest_framework import serializers
from .models import Api, Categoria


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
