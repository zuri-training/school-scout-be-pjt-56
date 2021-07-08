# Generated by Django 3.2.4 on 2021-07-08 08:29

import autoslug.fields
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
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name')),
                ('overview', models.TextField()),
                ('program', models.CharField(choices=[('BSc', "Bachelor's Degree"), ('MSc', "Master's Degree"), ('PhD', 'Doctorate Degree')], max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to=None)),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=234, null=True)),
                ('students', models.IntegerField(blank=True, null=True)),
                ('financial_aid', models.TextField()),
                ('hostel', models.TextField()),
                ('has_hostel', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Name of Faculty', max_length=150, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='core.school')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Department name', max_length=150, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to='core.faculty')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='core.article')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
