# Generated by Django 5.0.6 on 2024-05-27 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20240527_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'CREATOR'}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]
