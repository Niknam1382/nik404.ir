# Generated by Django 5.0.7 on 2024-07-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonium', '0005_videofile_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videofile',
            old_name='subject',
            new_name='discription',
        ),
        migrations.AddField(
            model_name='videofile',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videofile',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videofile',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='videofile',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videofile',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videofile',
            name='title',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
