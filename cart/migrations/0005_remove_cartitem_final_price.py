# Generated by Django 5.0.7 on 2024-08-08 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem_final_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='final_price',
        ),
    ]
