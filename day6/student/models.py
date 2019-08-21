from django.db import models

# Create your models here.
# # 自定义模型管理器
# class StudentInfoManager(models.Manager):
#     # 修改管理器返回的原始查询集合
#     def all(self):
#         # 重写all 方法，返回性别='girl'的学生
#         return super(StudentInfoManager,self).all().filter(gender = 'girl')
#
#     # 在模型类中自定义创建对象方法
#     def create_object(self,name,age,gender):
#         # 创建学生对象
#         student = StudentInfo()
#         # 获取数据
#         student.name = name
#         student.age = age
#         student.gender = gender
#         student.save()
#         return student

class Banclass(models.Model):
    '''班级信息'''
    banname = models.CharField(max_length=20,verbose_name='班级名称')

    def __str__(self):
        return self.banname

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name

class StudentInfo(models.Model):
    '''学生信息'''
    name = models.CharField(max_length=20,verbose_name='学生姓名')
    age = models.IntegerField(verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl','女'),('boy','男')),default='girl',max_length=6,verbose_name='学生性别')
    ban = models.ForeignKey(Banclass,verbose_name='所属班级')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

class StudentId(models.Model):
    '''学号信息'''
    stuid = models.CharField(max_length=20,verbose_name='学号')
    student = models.OneToOneField(StudentInfo,verbose_name='所属学生')

    def __str__(self):
        return self.stuid

    class Meta:
        verbose_name = '学号信息'
        verbose_name_plural = verbose_name