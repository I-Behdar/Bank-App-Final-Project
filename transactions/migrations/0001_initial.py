# Generated by Django 4.0.6 on 2022-08-09 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='transaction date')),
                ('amount', models.FloatField()),
                ('source_account_id', models.PositiveIntegerField()),
                ('target_account_id', models.PositiveIntegerField()),
                ('source_account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_account', to='contenttypes.contenttype')),
                ('target_account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_account', to='contenttypes.contenttype')),
            ],
        ),
    ]
