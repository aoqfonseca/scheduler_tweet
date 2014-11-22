from django.db import models

class Tweet(models.Model):

	texto = models.TextField(max_length=200)
	agendado_para = models.DateTimeField(u'Agendado para')
	publicado = models.BooleanField(default=False)
