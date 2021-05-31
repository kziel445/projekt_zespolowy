from django.contrib.auth.models import AbstractUser
from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.validators import RegexValidator
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()
    image = models.URLField


class User(AbstractUser):
    city = models.CharField(max_length=50,blank=True)
    street = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=6, blank=True, validators=[RegexValidator(
        regex='^[0-9]{2}-[0-9]{3}$',
        message='Zip code Must be in xx-xxx format',
        code='invalid_zipcode'
    ),
    ])
    house_number = models.CharField(max_length=6, blank=True)
    flat_number = models.CharField(max_length=6, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank= True, editable=False)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return f'/{self.slug}'



class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True, blank= True,editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True)
    amount = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='media/productImages/')
    thumbnail = models.ImageField(upload_to='media/productThumbnails/', blank=True, null=True,editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(400, 200)):
        img = Image.open(image)
        if img.mode in ("RGBA", "P"):
            img.convert('RGB')

        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at', ]

        def __str__(self) -> str:
            return self.user.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=1)

    def __str__(self) -> str:
        return '%s' % self.id




