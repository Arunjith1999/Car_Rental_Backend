# Generated by Django 4.2 on 2023-05-30 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renter_Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renters.renters')),
            ],
        ),
    ]
