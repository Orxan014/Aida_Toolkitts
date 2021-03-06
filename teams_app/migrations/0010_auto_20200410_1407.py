# Generated by Django 3.0.4 on 2020-04-10 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams_app', '0009_team_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='document',
        ),
        migrations.CreateModel(
            name='TeamDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams_app.Team')),
            ],
        ),
    ]
