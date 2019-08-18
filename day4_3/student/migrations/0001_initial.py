# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('banid', models.CharField(verbose_name='班级名称', max_length=20)),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
            },
        ),
        migrations.CreateModel(
            name='StudentId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stuid', models.CharField(verbose_name='学号', max_length=20)),
            ],
            options={
                'verbose_name': '学号信息',
                'verbose_name_plural': '学号信息',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='学生姓名', max_length=20)),
                ('age', models.IntegerField(verbose_name='学生年龄', default=18)),
                ('gender', models.CharField(verbose_name='学生性别', max_length=6, default='girl', choices=[('girl', '女'), ('boy', '男')])),
                ('addtime', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('ban', models.ForeignKey(verbose_name='所属班级', to='student.Ban')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
        migrations.AddField(
            model_name='studentid',
            name='student',
            field=models.OneToOneField(verbose_name='所属学生', to='student.StudentInfo'),
        ),
    ]
