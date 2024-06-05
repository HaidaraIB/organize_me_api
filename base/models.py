from django.db import models
# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)

class Bill(models.Model):
    payment_amount = models.FloatField()
    commission_amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField(default='11:11')
    provider = models.CharField(max_length=100, blank=False, null=False)
    operation_number = models.CharField(max_length=100, blank=False, null=False)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

    class Meta:
        abstract=True

class ElectricBill(Bill):
    gov = models.CharField(max_length=100, blank=False, null=False)
    billing_number = models.CharField(max_length=100, blank=False, null=False)
    invoice_number = models.CharField(max_length=100, blank=False, null=False)
    subscription_number = models.CharField(max_length=100, blank=False, null=False)

class WaterBill(Bill):
    gov = models.CharField(max_length=100, blank=False, null=False)
    receipt_number = models.CharField(max_length=100, blank=False, null=False)
    barcode_number = models.CharField(max_length=100, blank=False, null=False)
    counter_number = models.CharField(max_length=100, blank=False, null=False)

class TelecomBill(Bill):
    phone_number_email = models.CharField(max_length=100, blank=False, null=False)
    invoice_number = models.CharField(max_length=100, blank=False, null=False)