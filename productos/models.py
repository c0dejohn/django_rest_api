from django.db import models


class Cerveza(models.Model):
     marca = models.CharField(max_length=255)
     alcohol = models.DecimalField(max_digits=4,decimal_places=2)
     mililitros =models.IntegerField()
     artesanal = models.BooleanField()
     nacionalidad = models.CharField(max_length=255, blank=True, null=True)
     creado = models.DateTimeField(auto_now=True)
     editado = models.DateTimeField(auto_now=True)
     
     def __str__(self):
         return self.marca
