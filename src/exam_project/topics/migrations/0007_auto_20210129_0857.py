# Generated by Django 3.1.4 on 2021-01-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_auto_20210128_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='status',
            field=models.IntegerField(choices=[(0, 'OFF'), (1, 'LIVE')], default=0),
        ),
    ]