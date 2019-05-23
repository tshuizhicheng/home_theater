from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('userName','userRegisterTime','userValidTime','userGrant','userPreference')
    list_display_links = ('userName','userRegisterTime','userValidTime','userGrant','userPreference')

    fieldsets = (
        ('基本信息',{
            'fields':('userName','userValidTime','userGrant','userPreference')
        }),
    )


class FilmAdmin(admin.ModelAdmin):
    list_display = ('filmName','filmBrief','filmType','filmRelease_time','filmPlay_times','filmLove','filmWeight')
    list_display_links = ('filmName','filmBrief','filmType','filmRelease_time','filmPlay_times','filmLove','filmWeight')
    fieldsets = (
        ('基本信息',{
            'fields':('filmName','filmBrief','filmType','filmRelease_time','filmPlay_times','filmLove','filmWeight')
        }),
        ('更多',{
            'fields':('filmCover','filmPurl','filmPermisson','filmIsTop')
        })
    )




admin.site.register(User,UserAdmin)
admin.site.register(Film,FilmAdmin)


