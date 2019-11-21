# Generated by Django 2.2.7 on 2019-11-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20191121_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='createevent',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default=None, max_length=50),
            preserve_default=False,
        ),
    ]
