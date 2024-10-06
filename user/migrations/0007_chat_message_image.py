# Generated by Django 5.1.1 on 2024-10-06 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_chat_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_message',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.chat_images'),
        ),
    ]
