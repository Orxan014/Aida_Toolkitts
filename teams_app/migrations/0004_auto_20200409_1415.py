# Generated by Django 3.0.4 on 2020-04-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams_app', '0003_auto_20200409_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=255),
        ),
    ]
