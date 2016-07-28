from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	GENEROS = (
			('H','HOMBRE'),
			('M','MUJER'),
		)
	usuario = models.OneToOneField(User)
	foto = models.ImageField(upload_to='img')
	bio = models.TextField()
	empresa = models.CharField(max_length=140)
	genero = models.CharField(max_length=5, choices=GENEROS)

	def __str__(self):
		return 'este perfil pertenece a {}'.format(self.usuario)