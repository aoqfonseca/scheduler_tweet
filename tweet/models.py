# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from twython import Twython


class Configuracao(models.Model):

    dono = models.ForeignKey(User)
    app_key = models.CharField(max_length=200)
    app_secret = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s ' % (self.app_key, self.app_secret)

    def __str__(self):
        return u'%s - %s ' % (self.app_key, self.app_secret)


class Tweet(models.Model):

    texto = models.TextField(max_length=200)
    agendado_para = models.DateTimeField(u'Agendado para')
    publicado = models.BooleanField(default=False)
    configuracao = models.ForeignKey(Configuracao, null=True)

    def send(self):

        client = Twython(self.configuracao.app_key,
                         self.configuracao.app_secret,
                         self.configuracao.token,
                         self.configuracao.token_secret)

        print "sending %s" % self.texto

        self.publicado = True
        client.update_status(status=self.texto)
        self.save()
