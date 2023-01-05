from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Comments)
admin.site.register(Customer)
admin.site.register(UserList)
admin.site.register(ListedMovie)

