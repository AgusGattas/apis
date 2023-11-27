from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Api(models.Model):
    API = models.CharField(primary_key=True, max_length=6)
    Description = models.CharField(max_length=50)
    Auth = models.PositiveSmallIntegerField()
    HTTPS = models.BooleanField(default=False)
    Cors = models.BooleanField(default=False)
    Link = models.URLField()
    Category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.API
