from django.db import models

class Pets(models.Model):
	# питомцы
	name = models.CharField('Питомцы', max_length=20, unique=True)
	url = models.SlugField(max_length=30, unique=True)
	draft = models.BooleanField('Черновик', default=False)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Питомцы'
		verbose_name_plural = 'Питомец'
