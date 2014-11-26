# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_tweet_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracao',
            name='app_key',
        ),
        migrations.RemoveField(
            model_name='configuracao',
            name='app_secret',
        ),
        migrations.AddField(
            model_name='configuracao',
            name='nome',
            field=models.CharField(default=b'ainda nao definido', max_length=200),
            preserve_default=True,
        ),
    ]
