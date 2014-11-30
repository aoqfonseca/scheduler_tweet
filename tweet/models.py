# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from twython import Twython


class Configuracao(models.Model):

    dono = models.ForeignKey(User)
    nome = models.CharField(max_length=200, default='ainda nao definido')
    token = models.CharField(max_length=200)
    token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Tweet(models.Model):

    texto = models.TextField(max_length=200)
    agendado_para = models.DateTimeField(u'Agendado para')
    publicado = models.BooleanField(default=False)
    configuracao = models.ForeignKey(Configuracao, null=True)
    autor = models.ForeignKey(User, null=True)

    def send(self):

        client = Twython(settings.APP_KEY,
                         settings.APP_SECRET,
                         self.configuracao.token,
                         self.configuracao.token_secret)

        self.publicado = True
        client.update_status(status=self.texto)
        self.save()
