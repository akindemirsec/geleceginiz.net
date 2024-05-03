# admin.py dosyası
from django.contrib import admin
from .models import Gn_user

class GnUserAdmin(admin.ModelAdmin):
    list_display = ['userid', 'name', 'surname', 'mail', 'username']  # Liste görünümünde hangi alanların görüntüleneceğini belirtin

admin.site.register(Gn_user, GnUserAdmin)
