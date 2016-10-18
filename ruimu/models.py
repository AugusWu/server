#encoding=utf-8
from django.db import models

class BrandActivity(models.Model):
	class Meta:
		verbose_name = '品牌活动'
		verbose_name_plural = '品牌活动'

	title = models.CharField('活动标题', max_length=100)
	published = models.DateTimeField('发布时间')

class BrandText(models.Model):
	class Meta:
		verbose_name = '活动正文'
		verbose_name_plural = '活动正文'

	text = models.TextField('正文')
	activity = models.ForeignKey('BrandActivity')

class BrandImage(models.Model):
	class Meta:
		verbose_name = '活动图片'
		verbose_name_plural = '活动图片'

	image = models.ImageField('图片', upload_to='brand', max_length=512)
	activity = models.ForeignKey('BrandActivity')

class Product(models.Model):
	class Meta:
		verbose_name = '产品'
		verbose_name_plural = '产品'

	name = models.CharField('名称', max_length=100)
	mode = models.CharField('规格', max_length=100)

class ProductImage(models.Model):
	class Meta:
		verbose_name = '产品图片'
		verbose_name_plural = '产品图片'

	image = models.ImageField('图片', upload_to='product', max_length=512)
	product = models.ForeignKey('Product')	
