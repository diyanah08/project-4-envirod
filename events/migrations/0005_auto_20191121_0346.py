# Generated by Django 2.2.7 on 2019-11-21 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_createevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createevent',
            old_name='cost',
            new_name='cost_per_pax',
        ),
    ]
