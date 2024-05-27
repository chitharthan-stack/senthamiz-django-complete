from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


STATUS={
    ("draft","draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
    ("published","Published"),
}

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id ,filename)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    cid =ShortUUIDField(unique=True, length=10 , max_length=30, prefix="test", alphabet="SRE0123456789")
    title = models.CharField(max_length=100,default="Title")
    image = models.ImageField(upload_to=user_directory_path,default="image jpg ")
    class Meta:
        verbose_name_plural = "Categories"
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" >'%(self.image.url))
    def __str__(self):
        return self.title
    
class Product (models.Model):
    pid =ShortUUIDField(unique=True, length=10 , max_length=20, prefix="test", alphabet="SRE0123456789")
    title = models.CharField(max_length=100,default="Title")
    image = models.ImageField(upload_to=user_directory_path,default="image jpg ")
    description = models.TextField(null=True,blank=True,default="Description")

    address = models.TextField(null=True,blank=True,default="Description")

    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,default="product category",related_name="category")
    price = models.DecimalField(max_digits=999999999, decimal_places=2 ,default="0.00")
    specification = models.TextField(null=True,blank=True,default="Description") 
    product_status = models.CharField(choices=STATUS,max_length=10,default="in_review")

    status = models.BooleanField(default=True)
    featured = models.BooleanField (default=False)

    sku =ShortUUIDField(unique=True, length=4 , max_length=10, prefix="SKU-", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    upddated = models.DateTimeField (null=True,blank= True)

    # New field to store special features as a comma-separated list
    special_features = models.TextField(null=True, blank=True, help_text="Enter special features separated by commas")

    # New field to indicate DTCP approval
    dtcp_approved = models.BooleanField(default=False, help_text="Check if the product is DTCP approved")

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" >'%(self.image.url))
    
    def __str__(self):
        return self.title
    


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images" ,default="image.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,related_name="p_images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    
