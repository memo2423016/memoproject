from django.contrib import admin
from .models import Category, MemoPreserve

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class MemoPreserveAdmin(admin.ModelAdmin):
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(MemoPreserve, MemoPreserveAdmin)
