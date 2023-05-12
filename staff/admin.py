from django.contrib import admin
from staff.models import User,Employee,Incharge
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Employee)
admin.site.register(Incharge)

