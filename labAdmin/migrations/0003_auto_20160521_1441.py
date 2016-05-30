# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labAdmin', '0002_auto_20160421_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weekday_start', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0)),
                ('weekday_end', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0)),
                ('hour_start', models.TimeField()),
                ('hour_end', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Category_Device',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='device',
            old_name='category_device',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='category_devices',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='endSubcription',
            new_name='endSubscription',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='needSubcription',
            new_name='needSubscription',
        ),
        migrations.RemoveField(
            model_name='logerror',
            name='nfc',
        ),
        migrations.RemoveField(
            model_name='role',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='hour_end',
        ),
        migrations.RemoveField(
            model_name='role',
            name='hour_start',
        ),
        migrations.RemoveField(
            model_name='role',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='role',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='device',
            name='mac',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logerror',
            name='code',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='logerror',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='nfcId',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='role',
            name='time_slots',
            field=models.ManyToManyField(to='labAdmin.TimeSlot'),
        ),
    ]
