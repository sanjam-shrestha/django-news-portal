from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    page_views=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='News'
