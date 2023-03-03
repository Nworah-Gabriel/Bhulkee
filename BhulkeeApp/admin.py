from django.contrib import admin
from .models import User, MailLists, Messages

# Register your models here.
admin.site.register(User)
admin.site.register(MailLists)
admin.site.register(Messages)