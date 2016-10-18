from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response

from .models import Product
from .models import BrandActivity

# Create your views here.
def home_view(request):
	return render_to_response('index.html', {'page_name': 'index'})

def product_view(request):
	queryset = Product.objects.all()
	return render_to_response('product.html', {'page_name': 'product', 'product_list': queryset})

def product_detail(request, id):
	p = get_object_or_404(Product, id=id)
	return render_to_response('pdetail.html', {'product':p})

def brand_view(request):
	queryset = BrandActivity.objects.order_by('-published')
	return render_to_response('brand.html', {'page_name': 'brand', 'brand_list': queryset})

def brand_detail(request, id):
	ba = get_object_or_404(BrandActivity, id=id)
	images = ba.brandimage_set.all()
	paras = ba.brandtext_set.all()

	paragraph = []
	for i in range(max(len(images), len(paras))):
		img = text = None
		if i < len(images):
			img = images[i].image
		if i < len(paras):
			text = paras[i].text
		paragraph.append((text, img))
	print(paragraph)
	return render_to_response('bdetail.html', {'brand':ba, 'para':paragraph})

def about_view(request):
	return render_to_response('about.html', {'page_name': 'about'})
