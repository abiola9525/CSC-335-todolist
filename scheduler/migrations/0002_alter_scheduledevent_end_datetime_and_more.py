# Generated by Django 4.2.2 on 2025-05-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledevent',
            name='end_datetime',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='scheduledevent',
            name='start_datetime',
            field=models.CharField(max_length=255),
        ),
    ]
