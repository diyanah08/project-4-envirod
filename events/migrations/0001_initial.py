# Generated by Django 2.2.4 on 2019-11-20 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('sku', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Location')),
                ('tags', models.ManyToManyField(to='events.Tag')),
            ],
        ),
    ]
