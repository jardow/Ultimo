from django.db import models


# Create your models here.





class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
