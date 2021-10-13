from django.contrib import admin

# Register your models here.

from .models import Category, Kakeibo

# 追加


class KakeiboAdmin(admin.ModelAdmin):
    # Adminの表示を設定
    list_display = ('date', 'category', 'money', 'memo')


admin.site.register(Category)
admin.site.register(Kakeibo, KakeiboAdmin)  # 修正
