# Generated by Django 5.0.6 on 2024-07-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='poto_profil',
            new_name='photo_profil',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'CREATEUR'), ('SUBSCRIBER', 'Abonné')], max_length=30, verbose_name='Rôle'),
        ),
    ]
