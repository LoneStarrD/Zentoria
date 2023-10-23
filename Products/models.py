from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategory')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Style(models.Model):
    style = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.style


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_images/')
    specification = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True)
    style_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def generate_style_code(self):
        if self.style:
            code_length = 10
            alphanumeric_characters = string.ascii_letters + string.digits
            return ''.join(random.choice(alphanumeric_characters) for _ in range(code_length))
        return ""

    def save(self, *args, **kwargs):
        if not self.style_code:
            self.style_code = self.generate_style_code
        super().save(*args, **kwargs)


class ProductAttribute(models.Model):
    attribute_type = models.CharField(max_length=50)
    attribute_value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.attribute_type}: {self.attribute_value}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    review_image = models.ImageField(upload_to='review_images/', null=True, blank=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"


class FavouriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Favourite: {self.product.name}"
