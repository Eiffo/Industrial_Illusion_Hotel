# Generated by Django 5.2 on 2025-05-13 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_room_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room_Count',
            new_name='RoomCount',
        ),
    ]
