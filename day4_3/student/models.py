from django.db import models
from datetime import datetime

# Create your models here.
class Ban(models.Model):
    '''
    班级信息
    班级信息字段:班级名称
    '''
    banid = models.CharField(max_length=20,verbose_name='班级名称')

    def __str__(self):
        return self.banid

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name


class StudentInfo(models.Model):
    '''
    学生信息
    学生信息字段： 所属班级 姓名 年龄 性别 添加时间
    '''
    ban = models.ForeignKey(Ban,verbose_name='所属班级')
    name = models.CharField(max_length=20,verbose_name='学生姓名')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(max_length=6,choices=(('girl','女'),('boy','男')),default='girl',verbose_name='学生性别')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

class StudentId(models.Model):
    '''
    学号信息
    学号信息字段: 学号 所属学生
    '''
    stuid = models.CharField(max_length=20,verbose_name='学号')
    student = models.OneToOneField(StudentInfo,verbose_name='所属学生')

    def __str__(self):
        return self.stuid

    class Meta:
        verbose_name = '学号信息'
        verbose_name_plural = verbose_name


