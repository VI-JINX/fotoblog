# Generated by Django 5.0.6 on 2024-07-22 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_word_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Blog_set', to='blog.photo'),
        ),
    ]
