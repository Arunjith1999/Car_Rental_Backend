# Generated by Django 4.2 on 2023-05-30 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renters', '0001_initial'),
        ('superuser', '0002_alter_booking_end_date_alter_booking_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='renter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='renters.renters'),
        ),
    ]
