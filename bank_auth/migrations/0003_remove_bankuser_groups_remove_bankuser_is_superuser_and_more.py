# Generated by Django 4.0.4 on 2022-07-28 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_auth', '0002_bankuser_is_admin_alter_bankuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='bankuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='bankuser',
            name='user_permissions',
        ),
    ]
