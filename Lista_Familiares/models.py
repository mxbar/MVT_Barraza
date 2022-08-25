from django.db import models

class Familiar(models.Model):
    nombre=models.CharField('nombre', max_length=50)
    apellido=models.CharField('apellido', max_length=50)
    ocupacion=models.CharField('ocupacion', max_length=40, blank=True)
    nacimiento=models.DateField('fecha de nacimiento')
    dni=models.IntegerField('identificacion')

    def __str__(self):
        return self.nombre +' '+ self.apellido
    
