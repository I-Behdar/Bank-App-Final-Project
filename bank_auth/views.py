from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from bank_accounts.models import CurrentAccount, AbstractBankAccount, SavingsAccount, ForeignAccount
from .models import BankUser


class HomeView(View):
    def get(self, request):
        return render(request, "bank_auth/index.html")


class CreateProfileView(View):
    def get(self, request):
        context = {}
        return render(request, "bank_auth/create_profile.html", context)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password_1 = request.POST.get("pass1")
        password_2 = request.POST.get("pass2")

        if password_1 != password_2:
            messages.error(request, "Passwords do not match, please try again.")
            return redirect(reverse("create_profile"))

        clean_email = BankUser.objects.filter(email=email).exists()
        if clean_email:
            messages.error(request, "Email already exists, please try again.")
            return redirect(reverse("create_profile"))

        user = BankUser.objects.create(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password_1)
        user.save()

        CurrentAccount.objects.create(user=user,
                                      account_number=AbstractBankAccount.create_account_number())

        SavingsAccount.objects.create(user=user,
                                      account_number=AbstractBankAccount.create_account_number())

        ForeignAccount.objects.create(user=user,
                                      account_number=AbstractBankAccount.create_account_number())

        return render(request, "bank_auth/login.html")


class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, "bank_auth/login.html", context)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect(reverse("current_account"))
        else:
            messages.error(request, "Wrong email or password, please try again.")
            return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
