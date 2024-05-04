from django.contrib import admin
from django import forms
from .models import *

class GnUserAdmin(admin.ModelAdmin):
    list_display = ['userid', 'name', 'surname', 'mail', 'username']  

class GnFakulteAdmin(admin.ModelAdmin):
    list_display = ['fakulte_id', 'fakulte_name', 'get_universite']  

    def get_universite(self, obj):
        return obj.fakulte_uni.uni_name

    get_universite.short_description = "Üniversite"

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'bolum', 'description', 'video']  
    fields = ['name', 'bolum', 'description', 'video']  # Video alanını ekleyin

class GnBolumAdmin(admin.ModelAdmin):
    list_display = ['bolum_id', 'bolum_name', 'bolum_fakulte', 'get_universite_info']

    def get_universite_info(self, obj):
        return obj.bolum_fakulte.fakulte_uni.uni_name

    get_universite_info.short_description = "Üniversite"


class GnUniversiteAdmin(admin.ModelAdmin):
    list_display = ('uni_name', 'uni_city', 'uni_logo')

class BolumAdmin(admin.ModelAdmin):
    list_display = ('bolum_name', 'bolum_fakulte', 'bolum_universite')
    list_filter = ('bolum_fakulte', 'bolum_universite') 
    search_fields = ['bolum_name', 'bolum_fakulte__fakulte_name', 'bolum_universite__uni_name']  

# Modeller için admin sınıflarını kaydet
admin.site.register(Gn_user, GnUserAdmin)
admin.site.register(Gn_Fakulte, GnFakulteAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Gn_Bolum, GnBolumAdmin)
admin.site.register(Gn_universite, GnUniversiteAdmin)
