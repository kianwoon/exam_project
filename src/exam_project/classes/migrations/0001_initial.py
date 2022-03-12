# Generated by Django 3.1.4 on 2020-12-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('class_description', models.CharField(max_length=100)),
                ('class_level', models.IntegerField()),
            ],
            options={
                'db_table': 'classes',
            },
        ),
    ]