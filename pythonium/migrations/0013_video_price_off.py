# Generated by Django 5.0.7 on 2024-07-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonium', '0012_video_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='price_off',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
