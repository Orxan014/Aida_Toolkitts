# Generated by Django 3.0.4 on 2020-04-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards_app', '0003_auto_20200416_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='set_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]