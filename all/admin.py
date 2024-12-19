from django.contrib import admin
from .models import Driver, DriverRequest, Reklama


class DriverAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone_number', 'car_model', 'car_number', 'is_active')
    list_filter = ('is_active', 'car_model')
    search_fields = ('fio', 'phone_number', 'car_number')


class DriverRequestAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'phone_number', 'is_accepted', 'driver')
    list_filter = ('is_accepted',)
    search_fields = ('user_id', 'phone_number')


class ReklamaAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'from_location', 'to_location', 'passenger_count')
    list_filter = ('from_location', 'to_location')
    search_fields = ('telegram_id', 'from_location', 'to_location')


admin.site.register(Driver, DriverAdmin)
admin.site.register(DriverRequest, DriverRequestAdmin)
admin.site.register(Reklama, ReklamaAdmin)