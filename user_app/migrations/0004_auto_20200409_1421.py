# Generated by Django 3.0.4 on 2020-04-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20200409_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='./static/default.png', upload_to='', verbose_name='profilephoto'),
        ),
    ]
