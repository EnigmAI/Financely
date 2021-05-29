from django.contrib import admin
from .models import Client,Portfolio,Stock
# Register your models here.
admin.site.register(Client)
admin.site.register(Portfolio)
admin.site.register(Stock)
