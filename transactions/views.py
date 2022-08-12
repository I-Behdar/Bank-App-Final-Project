import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from bank_accounts.models import ForeignAccount, SavingsAccount, CurrentAccount
from transactions.models import Transaction


class TransactionView(View):
    def get(self, request):
        context = {}
        return render(request, "transactions/transaction.html", context)

    def post(self, request):
        amount = int(request.POST.get("amount"))
        transfer_from = request.POST.get("transfer_from")
        transfer_to = request.POST.get("transfer_to")

        current_account_id = CurrentAccount.objects.get(pk=request.user.id)
        savings_account_id = SavingsAccount.objects.get(pk=request.user.id)
        foreign_account_id = ForeignAccount.objects.get(pk=request.user.id)

        if transfer_from == transfer_to:
            messages.error(request, "Please choose different accounts.")
            return redirect("account_transactions")

        # success_message = messages.error(request, "Transfer successful.") DRY didn't work

        if transfer_from == "current" and transfer_to == "savings":
            transfer(source_account=current_account_id, target_account=savings_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("savings_account")

        if transfer_from == "current" and transfer_to == "foreign":
            transfer(source_account=current_account_id, target_account=foreign_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("foreign_account")

        if transfer_from == "savings" and transfer_to == "current":
            transfer(source_account=savings_account_id, target_account=current_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("current_account")

        if transfer_from == "savings" and transfer_to == "foreign":
            transfer(source_account=savings_account_id, target_account=foreign_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("foreign_account")

        if transfer_from == "foreign" and transfer_to == "current":
            transfer(source_account=foreign_account_id, target_account=current_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("current_account")

        if transfer_from == "foreign" and transfer_to == "savings":
            transfer(source_account=foreign_account_id, target_account=savings_account_id, amount=amount)
            messages.error(request, "Transfer successful.")
            return redirect("savings_account")


def transfer(source_account, target_account, amount):
    if amount <= 0:
        raise ValueError("Invalid transfer amount")

    if source_account.balance < amount:
        return "Not enough funds in your account"

    source_account.balance -= amount
    target_account.balance += amount

    source_account.save()
    target_account.save()

    Transaction.objects.create(source_account=source_account, target_account=target_account, amount=amount)


# def money_exchange(currency_from, currency_to, amount):
#     url = f"https://open.er-api.com/v6/latest/{currency_from}"
#     d = requests.get(url).json()
#     result = 0
#
#     if d["result"] == "success":
#         ex_target = d["rates"][currency_to]
#         result = ex_target * amount
#         result = "{:.2f}".format(result)
#
#     return result
