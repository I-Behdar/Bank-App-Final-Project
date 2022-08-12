import random

from django.contrib.contenttypes import fields
from django.db import models
from bank_auth.models import BankUser
from transactions.models import Transaction


class AbstractBankAccount(models.Model):
    user = models.OneToOneField(BankUser, on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    account_number = models.CharField(max_length=28, unique=True)

    class Meta:
        abstract = True

    @property
    def account_type(self):
        raise NotImplementedError

    @staticmethod
    def create_account_number():
        counter = 0
        digit_list = []
        while counter < 26:
            counter += 1
            digit = random.randrange(10)
            digit_list.append(str(digit))
        account_number = "".join(digit_list)
        return f"PL{account_number}"


class CurrentAccount(AbstractBankAccount):
    balance = models.FloatField(default=1000)
    transaction = fields.GenericRelation(Transaction)

    @property
    def account_type(self):
        return "Current"

    def __str__(self):
        return f"{self.user}, {self.account_type}, PLN {self.balance}"


class SavingsAccount(AbstractBankAccount):
    balance = models.FloatField(default=0)
    transaction = fields.GenericRelation(Transaction)

    @property
    def account_type(self):
        return "Savings"

    def __str__(self):
        return f"{self.user}, {self.account_type}, PLN {self.balance}"


class ForeignAccount(AbstractBankAccount):
    balance = models.FloatField(default=0)
    transaction = fields.GenericRelation(Transaction)

    @property
    def account_type(self):
        return "Foreign"

    def __str__(self):
        return f"{self.user}, {self.account_type}, EUR {self.balance}"
