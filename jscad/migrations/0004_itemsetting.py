# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jscad', '0003_auto_20140911_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('source', models.TextField(null=True, blank=True)),
                ('uri', models.URLField(null=True, blank=True)),
                ('item', models.ForeignKey(to='jscad.Item')),
                ('parent', models.ForeignKey(blank=True, to='jscad.ItemSetting', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
    ]
