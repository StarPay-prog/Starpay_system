# Generated by Django 5.0 on 2024-02-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_access_token_customsession_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsession',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('super_admin', 'super admin'), ('merchant', 'merchant')], max_length=32),
        ),
    ]
