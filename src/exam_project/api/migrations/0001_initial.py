# Generated by Django 3.1.4 on 2021-01-27 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_body', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(0, 'OFF'), (1, 'LIVE')], default=0)),
                ('valid_till', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 1, 27, 12, 43, 59, 778748))),
            ],
            options={
                'db_table': 'announcement',
                'managed': False,
            },
        ),
    ]
