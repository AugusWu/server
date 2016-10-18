# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruimu', '0002_auto_20150927_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='名称', max_length=100)),
                ('mode', models.CharField(verbose_name='规格', max_length=100)),
            ],
            options={
                'verbose_name_plural': '产品',
                'verbose_name': '产品',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(verbose_name='图片', max_length=512, upload_to='product')),
                ('product', models.ForeignKey(to='ruimu.Product')),
            ],
            options={
                'verbose_name_plural': '产品图片',
                'verbose_name': '产品图片',
            },
        ),
    ]
