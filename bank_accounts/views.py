from django.shortcuts import render
from django.views import View

from bank_accounts.models import CurrentAccount, SavingsAccount, ForeignAccount


# class CreateAccountView(View):
#     def post(self, request):
#         account_type = request.POST.get("account_type")
#
#         if account_type == "current":
#             try:
#                 if request.user.currentaccount:
#                     return HttpResponse("duplicate account")
#                 CurrentAccount.objects.create(user=request.user,
#                                               account_number=AbstractBankAccount.create_account_number())
#             except AbstractBankAccount.DoesNotExist:
#                 return HttpResponse("lets make one account")
#
#         if account_type == "savings":
#             if request.user.savingsaccount:
#                 return HttpResponse("duplicate account")
#             SavingsAccount.objects.create(user=request.user,
#                                           account_number=AbstractBankAccount.create_account_number())
#
#         if account_type == "foreign":
#             if request.user.foreignaccount:
#                 return HttpResponse("duplicate account")
#             ForeignAccount.objects.create(user=request.user,
#                                           account_number=AbstractBankAccount.create_account_number())
#
#         return render(request, "bank_accounts/current_account.html")


class CurrentAccountView(View):
    def get(self, request):
        current_account = CurrentAccount.objects.get(user=request.user)
        current_balance = current_account.balance
        context = {'current_balance': current_balance}
        return render(request, "bank_accounts/current_account.html", context)


class SavingsAccountView(View):
    def get(self, request):
        savings_account = SavingsAccount.objects.get(user=request.user)
        savings_balance = savings_account.balance
        print(savings_balance)
        context = {'savings_balance': savings_balance}
        return render(request, "bank_accounts/savings_account.html", context)


class ForeignAccountView(View):
    def get(self, request):
        foreign_account = ForeignAccount.objects.get(user=request.user)
        foreign_balance = foreign_account.balance
        context = {'foreign_balance': foreign_balance}
        return render(request, "bank_accounts/foreign_account.html", context)


