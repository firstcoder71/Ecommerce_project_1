from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIVISION_CHOICES = (
    ('', 'Choose Your Division'),
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    surname = models.CharField(max_length=200, null=True,blank=True)
    email = models.EmailField(max_length=200, null=True,blank=True)
    country = models.CharField(max_length=50, null=True,blank=True)
    area = models.CharField(choices=DIVISION_CHOICES, max_length=50, null=True,blank=True)
    state = models.CharField(max_length=50, null=True,blank=True)
    region = models.CharField(max_length=50, null=True,blank=True)
    address_line_1 = models.TextField(max_length=500, null=True,blank=True)
    address_line_2 = models.TextField(max_length=500, null=True,blank=True)
    postcode = models.IntegerField(default=1, null=True,blank=True)
    mobile_number = models.CharField(max_length=12,null=True,blank=True)
    image = models.ImageField(upload_to='profile_image', null=True,blank=True)
    

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('Dress', 'D'),
    ('Bag', 'B'),
    ('Shoes', 'S'),
    ('Accesories', 'A'),
    ('Best_Selling', 'BS'),
    ('Winter_Dress', 'WD'),
    ('All', 'AL'),
)

class Products(models.Model):
    title = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=12)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

