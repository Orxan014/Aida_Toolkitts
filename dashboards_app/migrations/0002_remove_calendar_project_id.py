# Generated by Django 3.0.4 on 2020-04-16 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='project_id',
        ),
    ]
