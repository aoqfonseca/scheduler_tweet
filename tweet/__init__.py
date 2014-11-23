from datetime import datetime
from pytz import timezone

from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler

from .models import Tweet


def tweet():
    tz = timezone(settings.TIME_ZONE)
    now = datetime.now(tz)
    tweets = Tweet.objects.filter(agendado_para__lte=now, publicado=False)
    for tweet in tweets:
        tweet.send()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tweet,
                      settings.SCHEDULE['type'],
                      minutes=settings.SCHEDULE['interval'],
                      id='tweet_jobs')

    scheduler.start()

start_scheduler()
