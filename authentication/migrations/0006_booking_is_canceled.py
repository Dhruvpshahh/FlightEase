# Generated by Django 5.0.6 on 2024-06-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_flight_booking_time_booking_booking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
    ]
