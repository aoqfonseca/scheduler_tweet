from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings

from twython import Twython
from tweet.models import Configuracao


def callback_twitter(request, configuracao_id):
    oauth_verifier = request.GET['oauth_verifier']
    configuracao = Configuracao.objects.get(id=configuracao_id)

    twitter = Twython(settings.APP_KEY, settings.APP_SECRET,
                      configuracao.token, configuracao.token_secret)

    response = twitter.get_authorized_tokens(oauth_verifier)

    configuracao.token = response.get('oauth_token')
    configuracao.token_secret = response.get('oauth_token_secret')
    configuracao.nome = response.get('screen_name')

    configuracao.save()

    return HttpResponse('Volte para a aplicacao')


def busca_token(self, configuracao_id):
    configuracao = Configuracao.objects.get(id=configuracao_id)

    twython = Twython(settings.APP_KEY, settings.APP_SECRET)

    callback_url = "%s/twitter/%s" % (settings.APP_URL, configuracao.id)
    response = twython.get_authentication_tokens(callback_url=callback_url)
    configuracao.token = response['oauth_token']
    configuracao.token_secret = response['oauth_token_secret']
    configuracao.save()

    return redirect(response['auth_url'])
