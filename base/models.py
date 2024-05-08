from django.db import models
import time
# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    last_el_bill = models.IntegerField(default=1)
    last_wa_bill = models.IntegerField(default=1)
    last_tel_bill = models.IntegerField(default=1)


class ElectricBill(models.Model):
    payment_amount = models.FloatField()
    commission_amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField(default='11:11')
    provider = models.CharField(max_length=100, blank=False, null=False, default='SyriatelSEP')
    operation_number = models.CharField(max_length=100, blank=False, null=False)

    gov = models.CharField(max_length=100, blank=False, null=False)

    billing_number = models.CharField(max_length=100, blank=False, null=False)
    invoice_number = models.CharField(max_length=100, blank=False, null=False)
    subscription_number = models.CharField(max_length=100, blank=False, null=False)

    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    

class WaterBill(models.Model):
    payment_amount = models.FloatField()
    commission_amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField(default='11:11')
    provider = models.CharField(max_length=100, blank=False, null=False, default='SyriatelSEP')
    operation_number = models.CharField(max_length=100, blank=False, null=False)

    gov = models.CharField(max_length=100, blank=False, null=False)

    receipt_number = models.CharField(max_length=100, blank=False, null=False)
    barcode_number = models.CharField(max_length=100, blank=False, null=False)
    counter_number = models.CharField(max_length=100, blank=False, null=False)

    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)


class TelecomBill(models.Model):
    payment_amount = models.FloatField()
    commission_amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField(default='11:11')
    provider = models.CharField(max_length=100, blank=False, null=False, default='SyriatelSEP')
    operation_number = models.CharField(max_length=100, blank=False, null=False)

    phone_number_email = models.CharField(max_length=100, blank=False, null=False)
    invoice_number = models.CharField(max_length=100, blank=False, null=False)
    
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)