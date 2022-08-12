from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateTimeField(verbose_name="transaction date", auto_now_add=True)
    amount = models.FloatField()

    source_account_type = models.ForeignKey(ContentType, related_name="source_account", on_delete=models.CASCADE)
    source_account_id = models.PositiveIntegerField()
    source_account = fields.GenericForeignKey("source_account_type", "source_account_id")

    target_account_type = models.ForeignKey(ContentType, related_name="target_account", on_delete=models.CASCADE)
    target_account_id = models.PositiveIntegerField()
    target_account = fields.GenericForeignKey("target_account_type", "target_account_id")
