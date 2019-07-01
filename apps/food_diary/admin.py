from django.contrib import admin

from .models import Food, FoodCategory, Portion


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "calories", "category")


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    list_display = ("food", "amount", "day", "meal")
