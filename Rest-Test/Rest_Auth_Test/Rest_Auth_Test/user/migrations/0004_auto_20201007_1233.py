# Generated by Django 3.1.1 on 2020-10-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='message',
            field=models.CharField(blank=True, max_length=88, verbose_name='message'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=88, unique=True, verbose_name='mobile'),
        ),
    ]
