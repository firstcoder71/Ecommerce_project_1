from django.shortcuts import render,redirect
from . models import Products,Customer,Cart,Contact
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages
from . forms import CustomerRegistration,CustomerProfileForm,ContactForm



# Create your views here.

def base(request):
    return render(request,'Shop/base.html')

class ProductView(View):
 def get(self, request):
  allproduct = Products.objects.all()
  return render(request, 'Shop/home.html', {'allproduct':allproduct})
 
class AllProductView(View):
   def get (self, request):
    allproduct = Products.objects.all()
    return render(request, 'Shop/all.html', {'allproduct':allproduct})   


class DresesProductView(View):
   def get (self, request):
    dresses = Products.objects.filter(category='Dress')
    return render(request, 'Shop/dresses.html', {'dresses':dresses})
   
#class Best_SellingProductView(View):
#    def get (self, request):
#     bestselling = Products.objects.filter(category='Best_Selling')
 #    return render(request, 'Shop/product-page.html', {'bestselling':bestselling})

class BagProductView(View):
   def get (self, request):
    bag = Products.objects.filter(category='Bag')
    return render(request, 'Shop/bags.html', {'bag':bag})
   
class ShoesProductView(View):
   def get (self, request):
    shoes = Products.objects.filter(category='Shoes')
    return render(request, 'Shop/shoes.html', {'shoes':shoes})
   
class AccesoriesProductView(View):
   def get (self, request):
    accesories = Products.objects.filter(category='Accesories')
    return render(request, 'Shop/accesories.html', {'accesories':accesories})
   
class AallProductView(View):
   def get (self, request):
    allp = Products.objects.all()
    return render(request, 'Shop/all products.html', {'all':allp})
   
class AallCategoryView(View):
   def get (self, request):
    allp = Products.objects.all()
    return render(request,'Shop/categories.html', {'alllp':allp})
    
#class WinterProductView(View):
  # def get (self, request):
  #  wintercollection = Products.objects.filter(category='Winter_Dress')
   # return render(request, 'Shop/winter collection.html', {'wintercollection':wintercollection})
   
def WinterProduct(request, data=None):
 
 if data == None:
  winter_collection = Products.objects.filter(category='Winter_Dress')
 elif data == 'Lubana' or data == 'Foring' or data == 'Twelve':
  winter_collection = Products.objects.filter(category='Winter_Dress').filter(brand=data)
 elif data == 'low_price':
   winter_collection = Products.objects.filter(category='Winter_Dress').filter(selling_price__lt=3200)
 elif data == 'high_price':
   winter_collection = Products.objects.filter(category='Winter_Dress').filter(selling_price__gt=3200)
 return render(request, 'Shop/winter_collection.html',{'wintercollection':winter_collection})

  




#def home(request):
#    return render(request,'Shop/home.html')

class CustormerRegistrationView(View):
   def get(self,request):
      form = CustomerRegistration()
      return render(request,'Shop/register.html',{'form':form})
   
   def post(self,request):
      form = CustomerRegistration(request.POST)
      if form.is_valid():
         messages.success(request, 'Congratulation your registration is sucessfully done')
         form.save()
      return render(request, 'Shop/register.html',{'form':form})
   
   
#def register(request):
#    return render(request,'Shop/register.html')

#def login(request):
#    return render(request,'Shop/login.html')

def shop_card(request):
    return render(request,'Shop/shopping-cart.html')
def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 10.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user==user ]
    if cart_product:
      for p in cart_product:
       tempamount = (p.quantity * p.product.discounted_price)
       amount +=  tempamount
       totalamount = amount + shipping_amount
      return render(request, 'Shop/shopping-cart.html', {'carts':cart, 'amount':amount,'totalamount':totalamount})
    else:
      return render(request, 'Shop/emptycard.html')

#def product_page(request):
#    return render(request,'Shop/product-page.html')
class product_page(View):
 def get(self, request, pk):
  product = Products.objects.get(pk=pk)
  bestselling = Products.objects.filter(category='Best_Selling')
  return render(request, 'Shop/product-page.html',{'product':product,'bestselling':bestselling})
 

#def contact(request):
#    return render(request,'Shop/contact.html')

#def categories(request):
#    return render(request,'Shop/categories.html')

def check_out(request):
    return render(request,'Shop/check-out.html')

def Profile(request):
    return render(request,'Shop/check-out.html')

class ProfileView(View):
 def get(self,request):
  form = CustomerProfileForm
  return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-primary'})

 def post(self,request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
     user = request.user
     name = form.cleaned_data['name']
     division = form.cleaned_data['division']
     district = form.cleaned_data['district']
     thana = form.cleaned_data['thana']
     vill = form.cleaned_data['vill']
     zip = form.cleaned_data['zip']
     reg = Customer(user=user,name=name,division=division,district=district,thana=thana,vill=vill,zip=zip)
     reg.save()
     messages.success(request,'Congratulation! Your profile perfectly update')
  return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-primary'})
 
 #contact view

class ContactView(View):
    def get(self,request):
        con_form = ContactForm()
        return render(request,'Shop/contact.html', {'con_form':con_form})
    
    def post(self, request):
      con_form = ContactForm(request.POST)
      if con_form.is_valid():
            user = request.user
            name = con_form.cleaned_data['name']
            email = con_form.cleaned_data['email']
            message = con_form.cleaned_data['message']
            con = Contact(user=user, name=name, email=email, message=message)
            con.save()
            messages.success(request,'Your message has been sent')
      return render(request,'Shop/contact.html', {'con_form':con_form})

