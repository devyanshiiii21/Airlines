# Generated by Django 4.1.7 on 2023-03-11 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.airport'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights.airport'),
        ),
    ]
