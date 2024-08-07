# Generated by Django 5.0.7 on 2024-07-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonium', '0002_alter_video_author_alter_video_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('videos', models.ManyToManyField(to='pythonium.videot')),
            ],
        ),
    ]
