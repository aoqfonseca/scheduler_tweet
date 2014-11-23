# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from twython import Twython


class Tweet(models.Model):

    texto = models.TextField(max_length=200)
    agendado_para = models.DateTimeField(u'Agendado para')
    publicado = models.BooleanField(default=False)

    def send(self):

        client = Twython(settings.TWEET['APP_KEY'],
                         settings.TWEET['APP_SECRET'],
                         settings.TWEET['OAUTH_TOKEN'],
                         settings.TWEET['OAUTH_TOKEN_SECRET'])

        print "sending %s" % self.texto

        self.publicado = True
        client.update_status(status=self.texto)
        self.save()
