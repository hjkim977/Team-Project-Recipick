# Generated by Django 3.2.25 on 2024-12-11 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_sender_id_message_sender_nick_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender_nick_name',
            new_name='sender_id',
        ),
    ]
