# Generated by Django 5.1.1 on 2024-10-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_chat_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_message',
            name='post_typing_status',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='chat_message',
            name='self_remove_status',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='chat_message',
            name='verify_status',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
