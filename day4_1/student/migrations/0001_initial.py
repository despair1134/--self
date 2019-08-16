# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='学生姓名', max_length=20)),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(verbose_name='学生性别', max_length=6, default='girl', choices=[('girl', '女'), ('boy', '男')])),
                ('addtime', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
    ]
