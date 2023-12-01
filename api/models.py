from django.db import models

# Create your models here.


class Categoria(models.Model):
    """modelo Categoria"""
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Api(models.Model):
    """modelo Categoria"""
    API = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Auth = models.CharField(max_length=20, null=True, blank=True)
    HTTPS = models.BooleanField(default=False)
    Cors = models.BooleanField(default=False)
    Link = models.URLField()
    Category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.API
