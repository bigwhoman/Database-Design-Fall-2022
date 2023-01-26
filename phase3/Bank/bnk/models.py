from django.db import models

class BaseUser(models.Model):
    id = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)        
    class Meta:
        abstract = True
class Customer(BaseUser):    
    ...

class Account(models.Model):
    credit = models.IntegerField()
    account_number = models.CharField(max_length=20, primary_key=True)
    customer = models.ForeignKey(Customer, related_name="account", on_delete=models.CASCADE)
class Employee(BaseUser):
    ...
class Salon(models.Model):
    employee = models.ForeignKey(to=Employee, related_name="salons", on_delete=models.CASCADE)
    security_level = models.ForeignKey('SecurityLevel', on_delete=models.CASCADE)

class SafeBox(models.Model):
    safebox_number = models.IntegerField()
    salon = models.ForeignKey(Salon, related_name="safeboxes", on_delete=models.CASCADE)
    price_group = models.ForeignKey(to="PriceGroup", related_name="safeboxes", on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['salon', 'safebox_number'], 
                name='unique_salon_safebox_number_combination'
            )
        ]
        indexes = [
            models.Index(fields=['salon', 'safebox_number',]),
        ]

class PriceGroup(models.Model):
    group = models.IntegerField(primary_key=True)
    daily_cost = models.IntegerField()

class Contract(models.Model):    
    salon = models.ForeignKey(Salon, related_name="contracts", on_delete=models.CASCADE)
    safebox = models.ForeignKey(SafeBox, related_name="contracts", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name="contracts", on_delete=models.CASCADE)
    timeplan = models.ForeignKey("TimePlan", related_name= "contracts", on_delete=models.CASCADE)
    paid_amount = models.IntegerField()    
    start_date = models.DateTimeField()
    class Meta:
        indexes = [
            models.Index(fields=['salon', 'safebox']),
            models.Index(fields=['customer']),
        ]

class TimePlan(models.Model):
    time = models.IntegerField(choices=[(1,1),(3,3),(12,12)], default=1)
    discount = models.IntegerField(default=5)

class SecurityLevel(models.Model):
    level = models.IntegerField(primary_key=True)
    maximum_amount = models.IntegerField()
# Create your models here.
