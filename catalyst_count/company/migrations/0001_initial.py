# Generated by Django 5.0.9 on 2024-11-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('year_founded', models.FloatField(blank=True, null=True)),
                ('industry', models.CharField(max_length=255)),
                ('size_range', models.CharField(max_length=255)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
                ('current_employee_estimate', models.IntegerField(blank=True, null=True)),
                ('total_employee_estimate', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
