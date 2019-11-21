from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    user_account = models.CharField(verbose_name="用户账号", max_length=25,primary_key=True)
    user_name = models.CharField(verbose_name="用户姓名", max_length=11)
    email = models.EmailField(verbose_name="邮箱", max_length=50,unique=True)
    GENDER_IN_CHOICES = [('0', 'female'), ('1', 'male'), ]
    user_url = models.CharField(verbose_name="头像", max_length=255)
    gender = models.IntegerField(verbose_name="性别", choices=GENDER_IN_CHOICES)
    phone = models.CharField(verbose_name="手机号", max_length=11)
    credit = models.IntegerField(verbose_name="用户积分", default=0)
    last_login = " "

    USERNAME_FIELD = "user_account"
    REQUIRED_FIELDS = ["gender","email"]

    def __str__(self):
        return self.user_account

    class Meta:
        db_table = 'tb_user'
        verbose_name_plural = verbose_name = '用户'



class Type(models.Model):
    type_id = models.BigAutoField(verbose_name='类型id', max_length=255,primary_key=True)
    type_name = models.CharField(verbose_name='类型名称', max_length=20)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'tb_type'
        verbose_name_plural = verbose_name = '类型'


class Article(models.Model):
    article_id = models.BigAutoField( verbose_name='文章编号',max_length=100,primary_key=True)
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.TextField(verbose_name='内容')
    page_view = models.PositiveIntegerField(verbose_name='阅读数',default=0)
    create_time = models.DateTimeField(verbose_name='发表时间',auto_now_add=True)
    flag = models.IntegerField(verbose_name='是否是草稿', default=0)  # 标志位
    user_account = models.ForeignKey('User', models.DO_NOTHING, db_column='user_account')
    type = models.ForeignKey('Type', models.DO_NOTHING, to_field='type_id')

    def __unicode__(self):
        return self.article_id

    def __str__(self):
        return self.article_id

    class Meta:
        db_table = 'tb_article'
        ordering = ['create_time']  # 按时间排序
        verbose_name_plural = verbose_name = '文章'


