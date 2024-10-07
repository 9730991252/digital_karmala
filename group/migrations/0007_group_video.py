# Generated by Django 5.1.1 on 2024-10-07 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_leader_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.group')),
            ],
        ),
    ]
