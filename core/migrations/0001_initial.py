# Generated by Django 3.2.4 on 2021-06-29 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_affiliated', models.BooleanField(blank=True, default=True, null=True)),
                ('overview', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=235, null=True)),
                ('culture', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to=None)),
                ('school_ranking', models.IntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=234, null=True)),
                ('number_of_staff', models.IntegerField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=234, null=True)),
                ('mobile', models.CharField(blank=True, max_length=234, null=True)),
                ('email', models.EmailField(blank=True, max_length=234)),
                ('number_of_students', models.IntegerField(blank=True, null=True)),
                ('has_accomodation', models.BooleanField(default=True)),
                ('min_tuition', models.IntegerField(blank=True, null=True)),
                ('max_tuition', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
