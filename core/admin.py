# admin.py dosyası
from django.contrib import admin
from .models import *

class GnUserAdmin(admin.ModelAdmin):
    list_display = ['userid', 'name', 'surname', 'mail', 'username']  # Liste görünümünde hangi alanların görüntüleneceğini belirtin

admin.site.register(Gn_user, GnUserAdmin)
admin.site.register(Gn_universite)
admin.site.register(Gn_Fakulte)
admin.site.register(Course)
admin.site.register(Gn_Bolum)