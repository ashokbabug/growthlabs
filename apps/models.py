from ast import Sub
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.category_name}'
class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.sub_category_name}'
class App(models.Model):
    name  = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    points = models.IntegerField()

class ScreenShot(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    app = models.ForeignKey(App,on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='media')

    class Meta:
        unique_together = ('user', 'app',)