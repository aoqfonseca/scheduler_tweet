# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_key', models.CharField(max_length=200)),
                ('app_secret', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('token_secret', models.CharField(max_length=200)),
                ('dono', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='configuracao',
            field=models.ForeignKey(to='tweet.Configuracao', null=True),
            preserve_default=True,
        ),
    ]
