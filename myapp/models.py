from django.db import models


# Create your models here.


class Account(models.Model):
    #用户名
    username = models.CharField("用户名",max_length=20,primary_key=True)
    #密码
    password = models.CharField("密码",max_length=20)

class chat(models.Model):
    chat_id = models.CharField("对话id",max_length=20,primary_key=True)
    username = models.ForeignKey(to='Account',to_field='username',on_delete=models.CASCADE)
    chat_title = models.CharField("对话标题",max_length=100)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(to='chat',to_field='chat_id',on_delete=models.CASCADE)
    chat_choices = (
        (0,'question'),
        (1,'answer'),
    )
    chat_type = models.SmallIntegerField(verbose_name="对话类型", choices=chat_choices)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    chat_content = models.TextField()

class Prompt_fuction(models.Model):

     prompt_title =  models.CharField("示例标题",max_length=50)
     prompt_text = models.CharField("示例文本",max_length=200)
