# Generated by Django 4.0.4 on 2022-07-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bankuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]