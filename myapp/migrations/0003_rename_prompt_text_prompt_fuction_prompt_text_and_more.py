# Generated by Django 4.2.11 on 2024-03-27 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_message_chat_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prompt_fuction",
            old_name="Prompt_text",
            new_name="prompt_text",
        ),
        migrations.AlterField(
            model_name="message",
            name="chat_type",
            field=models.SmallIntegerField(
                choices=[(0, "question"), (1, "answer")], verbose_name="对话类型"
            ),
        ),
    ]