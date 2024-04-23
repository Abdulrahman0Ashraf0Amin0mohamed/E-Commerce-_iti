from django.contrib import admin

# Register your models here.

from library.models import Library,BorrowingModel
from accounts.models import CustomUser

admin.site.register(Library)

admin.site.register(BorrowingModel)

admin.site.register(CustomUser)

