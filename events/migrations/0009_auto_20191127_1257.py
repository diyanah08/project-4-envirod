# Generated by Django 2.2.7 on 2019-11-27 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0008_createevent_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createevent',
            name='owner',
        ),
        migrations.AddField(
            model_name='createevent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
