# Generated by Django 5.1.1 on 2024-10-07 06:23

import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_group_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_video',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='group_video',
            name='code',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
