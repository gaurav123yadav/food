from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=150)
    code=models.CharField(max_length=50)

class Category(models.Model):
    name=models.CharField(max_length=100)
    @staticmethod
    def getAllCategories():
        return Category.objects.all()
    
    def __str__(self):
            return(self.name)

class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    mrp=models.FloatField()
    onSale=models.BooleanField(default=False)
    image=models.FileField()
    description=models.TextField()
    favourite= models.BooleanField(default=False)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @staticmethod
    def getAllProducts(limit = 0):
        if(limit and limit > 0):
            return product.objects.all()[:limit]
        else:
            return product.objects.all()
        

    @staticmethod 
    def getBestSeller():
        return product.objects.filter(favourite = True)

    @staticmethod
    def getAllProductsByCategoryId(categoryId):
        if categoryId:
            return product.objects.filter(category_id = categoryId)
        else:
            return product.getAllProducts()

class Cart(models.Model):
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Order(models.Model):
    billing_address=models.CharField(max_length=300)
    country=models.CharField(max_length=100)
    email=models.TextField()
    phone=models.TextField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    amount=models.FloatField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=50,default="cod")

class Order_items(models.Model):
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField()                         