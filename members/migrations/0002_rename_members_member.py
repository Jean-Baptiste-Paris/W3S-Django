# Generated by Django 5.1.4 on 2024-12-30 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
