# Generated by Django 3.1.4 on 2020-12-30 03:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersBank',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('answer_desc', models.TextField()),
                ('flag', models.IntegerField()),
            ],
            options={
                'db_table': 'answers_bank',
                'managed': False,
            },
        ),
    ]
