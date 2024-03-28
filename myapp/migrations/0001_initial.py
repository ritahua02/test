# Generated by Django 4.2.11 on 2024-03-27 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "username",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        verbose_name="用户名",
                    ),
                ),
                ("password", models.CharField(max_length=20, verbose_name="密码")),
            ],
        ),
        migrations.CreateModel(
            name="chat",
            fields=[
                (
                    "chat_id",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        verbose_name="对话id",
                    ),
                ),
                ("chat_title", models.CharField(max_length=100, verbose_name="对话标题")),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.account"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prompt_fuction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prompt_title", models.CharField(max_length=50, verbose_name="示例标题")),
                ("Prompt_text", models.CharField(max_length=200, verbose_name="示例文本")),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "chat_type",
                    models.SmallIntegerField(
                        choices=[(0, "question"), (1, "answer")], verbose_name="对话类型"
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("chat_content", models.TextField()),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.chat"
                    ),
                ),
            ],
        ),
    ]
