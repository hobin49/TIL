# Generated by Django 3.2.13 on 2022-10-17 06:35

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
            ],
        ),
    ]
