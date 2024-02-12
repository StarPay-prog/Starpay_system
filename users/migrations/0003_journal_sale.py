# Generated by Django 5.0.1 on 2024-01-08 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_id', models.CharField(default='', max_length=256, unique=True)),
                ('agent_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Transaction_date', models.DateTimeField(auto_now=True)),
                ('Transaction_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Transaction_status', models.CharField(blank=True, choices=[('Success', 'Success'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Failed', 'Failed'), ('Pending', 'Pending'), ('Aborted', 'Aborted'), ('Unconfirmed', 'Unconfirmed'), ('Cancelled', 'Cancelled')], max_length=255, null=True)),
                ('Transaction_remark', models.CharField(default='', max_length=200)),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_Account', to=settings.AUTH_USER_MODEL)),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_Account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_id', models.CharField(default='', max_length=256, unique=True)),
                ('Transaction_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('commision', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Transaction_status', models.CharField(blank=True, choices=[('Success', 'Success'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Failed', 'Failed'), ('Pending', 'Pending'), ('Aborted', 'Aborted'), ('Unconfirmed', 'Unconfirmed'), ('Cancelled', 'Cancelled')], max_length=255, null=True)),
                ('sale_type', models.CharField(blank=True, choices=[('Local_Hotel', 'Inventory Hotel'), ('TripJack_Hotel', 'TripJack Hotel'), ('Local_Flights', 'Inventory Flights'), ('TripJack_Flights', 'TripJack Flights')], max_length=255, null=True)),
                ('Cancelled', models.BooleanField(default=False)),
                ('agent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
