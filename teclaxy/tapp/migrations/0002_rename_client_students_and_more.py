# Generated by Django 4.2.7 on 2024-09-23 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Students',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='ingredients',
            new_name='topics',
        ),
    ]
