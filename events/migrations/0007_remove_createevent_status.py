# Generated by Django 2.2.7 on 2019-11-21 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_createevent_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createevent',
            name='status',
        ),
    ]