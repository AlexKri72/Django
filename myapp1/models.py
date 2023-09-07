from django.db import models
from django.db.models import Manager


# Create your models here.
class GameModel(models.Model):
    result= models.CharField(max_length=10)
    played=models.DateTimeField(auto_now_add=True)

    objects= Manager()
    def __str__(self):
        return f'Результат игры: {self.result}, время: {self.played}'

    class Meta:
        ordering = ['-played']
    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]

class Autor(models.Model):
    name= models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()
    bd= models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Category(models.Model):
    category = models.CharField(max_length=100)

class Post(models.Model):
    title= models.CharField(max_length=200)
    post = models.TextField()
    publish_date= models.DateField(auto_now_add=True)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    views= models.IntegerField(default=0)
    publish= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.autor} - {self.title} - {self.publish}'

class Client(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.CharField(max_length=13)
    address= models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address}'

class Product(models.Model):
    name=models.CharField(max_length=100)
    description= models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)

class Order(models.Model):
    client= models.ForeignKey(Client,on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    sum=models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
