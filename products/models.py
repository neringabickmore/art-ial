from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Collection(models.Model):

    class Meta:
        verbose_name_plural = "Collections"

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    collection_name = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=800)
    author = models.CharField(max_length=254)
    dimensions = models.CharField(max_length=70, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    images_folder = models.ForeignKey('ImagesFolder', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    tag = models.ForeignKey('Tag', null=True, blank=True, on_delete=models.SET_NULL)
    ft_new = models.BooleanField(default=False, null=True, blank=True)
    ft_preview = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    class Meta:
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Image(models.Model):

    class Meta:
        verbose_name_plural = "Images"

    name = models.CharField(max_length=254)
    img = models.ImageField(null=True, blank=True) 
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class ImagesFolder(models.Model):

    class Meta:
        verbose_name_plural = "ImagesFolders"

    name = models.CharField(max_length=254)
    imgs = models.ManyToManyField('Image')

    def __str__(self):
        return self.name


