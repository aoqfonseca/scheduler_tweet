# -*- coding: utf-8 -*-
import os
from datetime import datetime
from pytz import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule_twitter.settings")

import django
from django.conf import settings

from apscheduler.schedulers.background import BlockingScheduler
from tweet.models import Tweet


def tweet():
    tz = timezone(settings.TIME_ZONE)
    now = datetime.now(tz)
    tweets = Tweet.objects.filter(agendado_para__lte=now, publicado=False)
    for tweet in tweets:
        tweet.send()


def start_scheduler():
    django.setup()
    scheduler = BlockingScheduler()
    print 'iniciando o blockingjob'
    print settings.SCHEDULE['type']
    print settings.SCHEDULE['interval']
    scheduler.add_job(tweet,
                      settings.SCHEDULE['type'],
                      minutes=settings.SCHEDULE['interval'],
                      id='tweet_jobs')

    scheduler.start()

start_scheduler()
