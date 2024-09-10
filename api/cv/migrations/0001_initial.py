# Generated by Django 5.1.1 on 2024-09-10 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Last Name')),
                ('about_me', models.CharField(max_length=500, null=True, verbose_name='About Me')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='Phone')),
                ('created_date', models.DateField(auto_now=True, verbose_name='Created Date')),
            ],
            options={
                'db_table': 'curriculum',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100, null=True, verbose_name='School')),
                ('degree', models.CharField(max_length=100, null=True, verbose_name='Degree')),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('grade', models.CharField(max_length=100, null=True, verbose_name='Grade')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Description')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='cv.curriculum')),
            ],
            options={
                'db_table': 'education',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('company_name', models.CharField(max_length=100, null=True, verbose_name='Company Name')),
                ('location', models.CharField(max_length=100, null=True, verbose_name='Location')),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Description')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='cv.curriculum')),
            ],
            options={
                'db_table': 'experience',
                'ordering': ['id'],
            },
        ),
    ]
