# Generated by Django 3.0.4 on 2020-04-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards_app', '0004_auto_20200416_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='Post_images/'),
        ),
    ]