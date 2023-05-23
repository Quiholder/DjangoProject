# Generated by Django 4.2.1 on 2023-05-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('Campus_Id', models.IntegerField(blank=True, default='')),
                ('State', models.CharField(blank=True, default='', max_length=2)),
            ],
        ),
    ]
