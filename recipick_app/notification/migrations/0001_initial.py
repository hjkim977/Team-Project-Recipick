# Generated by Django 3.2.25 on 2024-11-22 04:57

from django.db import migrations, models
import notification.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('contents', models.TextField()),
                ('announce_dt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='expiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=notification.models.expiration_image_file_path)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]