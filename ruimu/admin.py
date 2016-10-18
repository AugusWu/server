#encoding=utf-8
from django.contrib import admin

from .models import BrandActivity
from .models import BrandText
from .models import BrandImage

from .models import ProductImage
from .models import Product

class TextInline(admin.StackedInline):
	model = BrandText
	extra = 2

class ImageInline(admin.StackedInline):
	model = BrandImage
	extra = 2

class ActivityAdmin(admin.ModelAdmin):
	inlines = [TextInline, ImageInline]
	list_display = ('title', 'published')

class ProductImageInline(admin.StackedInline):
	model = ProductImage
	extra = 2

class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductImageInline]
	list_display = ('name', 'mode')

class RMTAdminSite(admin.AdminSite):
	site_header = '瑞木堂'

site = RMTAdminSite(name='adminrmt')

site.register(BrandText)
site.register(BrandImage)
site.register(BrandActivity, ActivityAdmin)

site.register(ProductImage)
site.register(Product, ProductAdmin)
