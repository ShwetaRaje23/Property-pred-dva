
from django.db import models

class Prop_User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)

class Property_Info(models.Model):
	prop_id = models.IntegerField()
	price = models.FloatField(default=0.0)
	no_bedrooms = models.IntegerField()

class Neighbourhood(models.Model):
	dist_school_prop = models.FloatField(default=0.0)
	dist_shopping_complex = models.FloatField(default=0.0)
	prop_id = models.OneToOneField(Property_Info, primary_key=True)


'''
- build models in this way where each of them correspond to a table
- You can refer to Django tutorials https://docs.djangoproject.com/en/1.8/topics/db/models/

'''