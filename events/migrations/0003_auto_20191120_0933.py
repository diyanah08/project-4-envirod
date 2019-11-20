# Generated by Django 2.2.7 on 2019-11-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191120_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
