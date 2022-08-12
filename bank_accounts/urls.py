from django.urls import path

from .views import CurrentAccountView, SavingsAccountView, ForeignAccountView

urlpatterns = [
    path("current_account/", CurrentAccountView.as_view(), name="current_account"),
    path("savings_account/", SavingsAccountView.as_view(), name="savings_account"),
    path("foreign_account/", ForeignAccountView.as_view(), name="foreign_account"),
]
