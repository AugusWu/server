# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruimu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandimage',
            name='image',
            field=models.ImageField(upload_to='brand', max_length=512, verbose_name='图片'),
        ),
    ]
