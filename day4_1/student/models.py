from datetime import datetime

from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='学生姓名')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(max_length=6,choices=(('girl','女'),('boy','男')),default='girl',verbose_name='学生性别')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name