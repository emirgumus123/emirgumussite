from django.contrib import admin
from .models import Slider , Haberler , Hizmetler , ContactMessage

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    ordering = ('order',)
    list_filter = ('order',)

@admin.register(Haberler)
class HaberlerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_filter = ('created_at',)

@admin.register(Hizmetler)
class HizmetlerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)


