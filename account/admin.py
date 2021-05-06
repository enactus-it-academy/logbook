from django.contrib import admin

from account.models import User, Owner, Employee

admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Employee)
