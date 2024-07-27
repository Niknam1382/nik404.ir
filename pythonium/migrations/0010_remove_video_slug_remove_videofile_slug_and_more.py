# Generated by Django 5.0.7 on 2024-07-27 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonium', '0009_comment_parent_python_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='videofile',
            name='slug',
        ),
        migrations.AlterField(
            model_name='python_comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]