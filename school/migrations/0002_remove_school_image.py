# Generated by Django 3.2.4 on 2021-07-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='image',
        ),
    ]