from django.urls import path

from transactions.views import TransactionView, TransactionHistoryView

urlpatterns = [
    path("transactions/", TransactionView.as_view(), name="account_transactions"),
    path("history/", TransactionHistoryView.as_view(), name="transactions_history"),
]
