from django.db import models
from django.contrib.auth.models import User


# Create your models here.
TYPE=(('Positive','Positive'),
       ('Negative','Negative') )




class Profile(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    balance=models.FloatField(default=0,null=True,blank=True)
    
    income=models.FloatField(default=0,null=True,blank=True)

    expense=models.FloatField(default=0,null=True,blank=True)
    
    def __str__(self):
        return str(self.user)


class Expense(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    amount=models.FloatField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    expense_type=models.CharField(max_length=100,choices=TYPE)


    def __str__(self):
        return (self.name)
    
