# Generated by Django 5.0.7 on 2024-07-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_w2'),
    ]

    operations = [
        migrations.AddField(
            model_name='w2',
            name='title',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
