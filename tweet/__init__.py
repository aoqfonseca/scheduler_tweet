import logging
from datetime import datetime
from pytz import timezone

from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler

from .models import Tweet


log  = logging.getLogger('schedulers')


def tweet():
    tz = timezone(settings.TIME_ZONE)
    now = datetime.now(tz)
    tweets = Tweet.objects.filter(agendado_para__lte=now, publicado=False)
    for tweet in tweets:
        tweet.send()


def start_scheduler():
    scheduler = BackgroundScheduler()
    log.info('Cadastrando o job')
    scheduler.add_job(tweet,
                      settings.SCHEDULE['type'],
                      minutes=settings.SCHEDULE['interval'],
                      id='tweet_jobs')

    scheduler.start()

log.info('Iniciando a agendador')
start_scheduler()
