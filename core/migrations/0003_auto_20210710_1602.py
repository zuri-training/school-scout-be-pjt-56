# Generated by Django 3.2.4 on 2021-07-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=96)),
                ('state_abbr', models.CharField(blank=True, max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='first_name',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
