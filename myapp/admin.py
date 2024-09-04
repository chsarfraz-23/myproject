from django.contrib import admin

from myapp.models import User, ProductTypes

admin.site.register(User)
admin.site.register(ProductTypes)