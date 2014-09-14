# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jscad', '0002_auto_20140911_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='parent',
            field=models.ForeignKey(blank=True, to='jscad.Configuration', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(blank=True, to='jscad.Item', null=True),
        ),
    ]
