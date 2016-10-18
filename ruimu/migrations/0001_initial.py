# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='活动标题', max_length=100)),
                ('published', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '品牌活动',
                'verbose_name_plural': '品牌活动',
            },
        ),
        migrations.CreateModel(
            name='BrandImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(verbose_name='图片', upload_to='')),
                ('activity', models.ForeignKey(to='ruimu.BrandActivity')),
            ],
            options={
                'verbose_name': '活动图片',
                'verbose_name_plural': '活动图片',
            },
        ),
        migrations.CreateModel(
            name='BrandText',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField(verbose_name='正文')),
                ('activity', models.ForeignKey(to='ruimu.BrandActivity')),
            ],
            options={
                'verbose_name': '活动正文',
                'verbose_name_plural': '活动正文',
            },
        ),
    ]
