# Generated by Django 4.1.3 on 2022-11-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='edad',
            new_name='Nacimiento',
        ),
    ]