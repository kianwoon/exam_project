# Generated by Django 3.1.4 on 2021-01-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20201223_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='desc',
            field=models.CharField(default='more than 10,000', max_length=200),
            preserve_default=False,
        ),
    ]