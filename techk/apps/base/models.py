from django.db import models

# Create your models here.
class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

class Books(models.Model):
	# id = models.IntegerField()
	category_id = models.ForeignKey(Categories,on_delete=models.CASCADE)
	title = models.CharField(max_length=300,null=True,blank=True)
	thumbnail_url = models.CharField(max_length=300,null=True,blank=True)
	price = models.IntegerField(null=True,blank=True)
	stock = models.BooleanField()
	product_description = models.CharField(max_length=1000,null=True,blank=True)
	upc = models.CharField(max_length=50,null=True,blank=True)
