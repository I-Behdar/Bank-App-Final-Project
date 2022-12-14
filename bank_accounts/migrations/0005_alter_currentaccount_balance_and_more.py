# Generated by Django 4.0.4 on 2022-07-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0004_alter_currentaccount_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentaccount',
            name='balance',
            field=models.FloatField(default=1000),
        ),
        migrations.AlterField(
            model_name='foreignaccount',
            name='balance',
            field=models.FloatField(default=1000),
        ),
        migrations.AlterField(
            model_name='savingsaccount',
            name='balance',
            field=models.FloatField(default=1000),
        ),
    ]
