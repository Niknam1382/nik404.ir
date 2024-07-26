# Generated by Django 5.0.7 on 2024-07-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_options_post_comment_counter_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply_to_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replys', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(to='blog.reply_to_user'),
        ),
    ]