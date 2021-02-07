# Generated by Django 3.0.4 on 2020-04-09 14:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='team',
            name='team_member',
            field=models.ManyToManyField(related_name='team_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='member',
        ),
        migrations.AddField(
            model_name='teammembers',
            name='member',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
