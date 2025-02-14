# Generated by Django 5.0.6 on 2024-07-21 16:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_user_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'CREATOR'}, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]
