from django.contrib import admin
from .models import *

class GnUserAdmin(admin.ModelAdmin):
    list_display = ['userid', 'name', 'surname', 'mail', 'username']  

class GnFakulteAdmin(admin.ModelAdmin):
    list_display = ['fakulte_id', 'fakulte_name', 'fakulte_uni']  

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'bolum', 'description', 'video_url']  

class GnBolumAdmin(admin.ModelAdmin):
    list_display = ['bolum_id', 'bolum_name', 'bolum_fakulte']  

class GnUniversiteAdmin(admin.ModelAdmin):
    list_display = ('uni_name', 'uni_city', 'uni_logo')

# Modeller için admin sınıflarını kaydet
admin.site.register(Gn_user, GnUserAdmin)
admin.site.register(Gn_Fakulte, GnFakulteAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Gn_Bolum, GnBolumAdmin)
admin.site.register(Gn_universite, GnUniversiteAdmin)
