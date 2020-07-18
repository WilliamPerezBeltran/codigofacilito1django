from django.db import models
from apps.adopcion.models import Persona

"""
relacion uno a muchos 
una persona puede tener muchas mascotas

relacion muchos a muchos
una vacuna se puede aplicar a muchas mascotas 
y una mascota puede tener muchas vacunas 
"""

class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna,blank=True)
	def __str__(self):
		return self.nombre


	








# Persona.objects.create(nombre="ramon ",apellido="calzadilla",edad=23,telefono="123654",email="william@gmail.com",domicilio="afafaf")


# # uno a muchos 
# m=Mascota(nombre="simon perrito",sexo="macho",edad_aproximada=2,fecha_rescate="2020-07-16",persona=p)
# m.save()

# # muchos a muchos

# >>> v1=Vacuna.objects.get(id=1)
# >>> v2=Vacuna.objects.get(id=2)
# >>> v1
# p=Persona.objects.get(id=1)
# m=Mascota(nombre="simon perrito",sexo="macho",edad_aproximada=2,fecha_rescate="2020-07-16",persona=p)
# >>> v1=Vacuna.objects.get(id=1)
# >>> v2=Vacuna.objects.get(id=2)
# # muchos a muchos
# m.vacuna.add(v1,v2)

# y aqui no es necesario hacer .save()


