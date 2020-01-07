from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
#@login_required(login_url ="/accounts/signup")
def home(request):
	products =Product.objects.all()
	#paginator = Paginator(products, 10)
	#page = request.GET.get('page')
	#products =paginator.get_page(page)
	return render(request, 'products/home.html', {'products':products})

@login_required(login_url ="/accounts/signup")
def create(request):
	if request.method =='POST':
			if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
				product =Product()
				product.title =request.POST['title']
				product.body =request.POST['body']

				if request.POST['url'].startswith('http://') or request.POST['url'].startswith('http://'):
					product.url = request.POST['url']
				else:
					product.url ='http://' + request.POST['url']

				product.image =request.FILES['image']
				product.icon =request.FILES['icon']
				product.pub_date =timezone.datetime.now()
				product.hunter =request.user
				product.save()
				return redirect('products/detail/' + str(product.id))
			else:
				return render(request, 'products/create.html', {'error':'Sorry all forms reuired'})
	else:
		return render (request, 'products/create.html')

@login_required(login_url ="/accounts/signup")
def detail(request, product_id):
	product=get_object_or_404(Product,pk=product_id)
	return render(request, 'products/detail.html',{'product':product})
	#context ={'product':product}


@login_required(login_url ="accounts/signup")
def upvotes(request, product_id):
	if request.method =='POST':
		product=get_object_or_404(Product, pk=product_id)
		product.vote_total +=1
		product.save()
		return redirect('/products/detail/' + str(product.id)) #or product.id for the products product product specific

def edx(request):
	return render(request, 'products/edx.html')
