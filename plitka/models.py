from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории',max_length=150,unique=True)
    slug = models.SlugField('Slug',max_length=50)
    images = models.ImageField(upload_to='category', default=None)
    description = models.CharField('Описание',max_length=500,default=None)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField('Название',max_length=150)
    image = models.ImageField(upload_to='item', default=None)
    size = models.CharField("Размер",max_length=150,default=None)
    count = models.CharField("Количество",max_length=150, default=None)
    description = models.CharField("Описание",max_length=150,default=None)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    slug = models.CharField('Ссылка',max_length=150,default=None)


    def __str__(self):
        return self.name

# class our_products(models.Model):
