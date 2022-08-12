from django.contrib import admin

from .models import CurrentAccount, ForeignAccount, SavingsAccount

admin.site.register(CurrentAccount)
admin.site.register(SavingsAccount)
admin.site.register(ForeignAccount)

