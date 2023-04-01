from django.contrib import admin
from .models import MyApp1, MyApp2, MyApp3

class MyAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(MyApp1, MyAppAdmin) 

class MyAppAdmin2(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(MyApp2, MyAppAdmin2)

class MyAppAdmin3(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(MyApp3, MyAppAdmin3)


