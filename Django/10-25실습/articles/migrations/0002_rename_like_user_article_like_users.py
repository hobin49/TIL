# Generated by Django 3.2.13 on 2022-10-24 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='like_user',
            new_name='like_users',
        ),
    ]
