from idlelib.history import History

from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from json import loads
from django.http import HttpResponse
from django.http import JsonResponse
from myapp.models import *
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Account.objects.filter(username=username):
            return JsonResponse({'code': -1, 'msg': '用户名已存在！'})

        user = Account.objects.create(username=username, password=password)
        user.save()
        if user.username:
            return JsonResponse({'code': 0, 'msg': '注册成功！'})
        return JsonResponse({'code': -3, 'msg': '注册失败！请重新尝试注册！'})
    return JsonResponse({'code': 1, 'msg': '请求方法只能是POST方法！'})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Account.objects.filter(username=username).get()
        if user:
            if user.password==password:
                return JsonResponse({'code': 0, 'msg': '登陆成功'})
            else:
                return JsonResponse({'code': -2, 'msg': '密码错误'})
        return JsonResponse({'code': -3, 'msg': '账户不存在，请先注册账户'})

def add_chat(request):
    if request.method == 'POST':
        chat_title = request.POST.get('chat_title')
        username = request.POST.get('username')
        chat_id=request.POST.get('chat_id')
        chat_content = request.POST.get('chat_content')
        chat_type = request.POST.get('chat_type')
        if not chat.objects.filter(chat_id=chat_id):
            new_chat=chat.objects.create(chat_id=chat_id,chat_title=chat_title, username_id=username)
            new_chat.save()
            return JsonResponse({'code':0,'msg':"对话加入成功"})
        one_call_chat = chat.objects.filter(chat_id=chat_id).first()
        new_message=Message.objects.create(chat_content=chat_content, chat=one_call_chat, chat_type=chat_type)
        new_message.save()
        return JsonResponse({'code': 0, 'msg': "消息加入成功"})

def get_history_chat(request):
    if request.method == 'POST':
        chat_title = request.POST.get('chat_title')
        messages=[]
        one_chat = chat.objects.filter(chat_title=chat_title).first()
        history_messages = Message.objects.filter(chat=one_chat).select_related('chat').order_by('create_time')
        for message in history_messages:
            if message.chat_type==0:
                message.chat_type='chatcar'
            else:
                message.chat_type='user'
            messages.append([message.chat_type, message.chat_content])
        return JsonResponse({'code': 0, '历史信息列表': messages})



def add_prompt_fuction(request):
    if request.method == 'POST':
        prompt_title = request.POST.get('prompt_title')
        prompt_text = request.POST.get('prompt_text')
        if not Prompt_fuction.objects.filter(prompt_title=prompt_title).exists():
            new_prompt_fuction = Prompt_fuction.objects.create(prompt_title=prompt_title,prompt_text=prompt_text)
            new_prompt_fuction.save()
        return JsonResponse({'code':0,
                             'prompt_title':new_prompt_fuction.prompt_title,
                             'prompt_text':new_prompt_fuction.prompt_text,
                            'prompt_msg':'示例promp存储成功'})


def get_prompt_fuction(request):
    prompt_text = Prompt_fuction.objects.all().order_by('?')[:8]
    prompt_fuctions=[]
    for prompt_fuction in prompt_text:
        prompt_fuctions.append([prompt_fuction.prompt_title,prompt_fuction.prompt_text])
    return  HttpResponse(prompt_fuctions)

def get_history_messages(request):
    if request.method == 'POST':
        chat_title = request.POST.get('chat_title')
        history_messages=Message.objects.filter(chat__chat_title=chat_title).order_by('create_time')
        for message in history_messages:
            print(message)
        return JsonResponse({'code': 0, 'msg': '获取对话数据成功'})
def delete_chat(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        chat.objects.filter(chat_id=chat_id).delete()
        return JsonResponse({'code':0,'msg':'对话删除成功'})

def delete_message(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        last_message = Message.objects.filter(chat_id=chat_id,chat_type=0).order_by('create_time').first()
        last_message.delete()
        return JsonResponse({'code': 0, 'msg': '消息删除成功'})
