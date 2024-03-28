from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("add_chat/", views.add_chat, name="add_chat"),
    path("delete_chat/", views.delete_chat, name="chat"),
    path("delete_message/", views.chat, name="delete_message"),
    path("get_history_chat/", views.get_history_chat, name="get_history_chat/"),
    path("add_prompt_fuction/", views.add_prompt_fuction, name="add_prompt_chat"),
    path("get_prompt_fuction/", views.get_prompt_fuction,name="get_prompt_fuction")
]
