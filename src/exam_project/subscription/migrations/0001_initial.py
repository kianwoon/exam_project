# Generated by Django 3.1.4 on 2020-12-25 08:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('rebate', models.DecimalField(decimal_places=0, max_digits=10)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
            ],
            options={
                'db_table': 'subscription',
            },
        ),
    ]
