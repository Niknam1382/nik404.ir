# Generated by Django 5.0.7 on 2024-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonium', '0004_videofile_remove_video_videofile_video_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='subject',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
