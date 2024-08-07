# Generated by Django 5.0.7 on 2024-07-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_w2_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='w2e',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.DeleteModel(
            name='w2',
        ),
    ]
