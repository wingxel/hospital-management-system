# Generated by Django 4.2.7 on 2023-11-27 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]
