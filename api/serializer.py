from rest_framework import serializers
from .models import Api, Categoria


class ApiSerializer(serializers.ModelSerializer):
    """Serializador de objeto Api"""
    class Meta:
        model = Api
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serializador de objeto Categoria"""
    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializador de objeto Categoria
        donde se agrega el atributo api_count para el endpoint /category-list
    """
    api_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Categoria
        fields = ["id", 'nombre', 'api_count']
