# Generated by Django 4.0.4 on 2022-07-31 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0008_alter_foreignaccount_type_alter_savingsaccount_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentaccount',
            name='type',
        ),
        migrations.RemoveField(
            model_name='foreignaccount',
            name='type',
        ),
        migrations.RemoveField(
            model_name='savingsaccount',
            name='type',
        ),
    ]
