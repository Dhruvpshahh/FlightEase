# Generated by Django 5.0.6 on 2024-06-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_flight_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='distance',
            field=models.FloatField(default=300),
        ),
    ]
