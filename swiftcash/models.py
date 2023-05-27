from __future__ import unicode_literals
from django.db import models

# Create your models here.
class login_details(models.Model):
    login_name   = models.CharField(max_length=20)
    password     = models.CharField(max_length=20)
    class Meta:
        db_table='login_table'

class Myform(models.Model):
    name         = models.CharField(max_length=20)
    login_name   = models.CharField(max_length=20)
    email        = models.EmailField(max_length=20)
    phone_number = models.BigIntegerField()
    password     = models.CharField(max_length=20)
    location     = models.CharField(max_length=20)
    adhaar_num   = models.BigIntegerField()
    bank_acc     = models.BigIntegerField()
    gender=[
        ('male','male'),
        ('female','female'),
    ]
    Gender       = models.CharField(choices=gender,max_length=7)
    date=models.DateField()
    class Meta():
        db_table='signup'

class bankdetails(models.Model):
    from_acc    = models.BigIntegerField()
    to_acc      = models.BigIntegerField()
    branch      = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    payee_name  = models.CharField(max_length=50)
    payee_acc   = models.BigIntegerField()
    cif         = models.IntegerField()
    date        = models.DateField()
    amount      =  models.BigIntegerField()
    ph_no       =  models.BigIntegerField()
    class Meta:
        db_table='bank_details'

class selfbank_det(models.Model):
    acc    = models.BigIntegerField()
    branch      = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    payee_name  = models.CharField(max_length=50)
    payee_acc   = models.BigIntegerField()
    cif         = models.IntegerField()
    date        = models.DateField()
    amount      =  models.IntegerField()
    ph_no       =  models.BigIntegerField()
    class Meta:
        db_table='selfbank_his'

class Card_details(models.Model):
    name    = models.CharField(max_length=50,null=False) 
    number  = models.BigIntegerField(null=False) 
    month   = models.IntegerField(null=False) 
    year    = models.IntegerField(null=False) 
    cvv     = models.IntegerField(null=False) 
    class Meta:
        db_table='credit_card_his'

class feedback(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    ph_no=models.BigIntegerField()
    subject=models.CharField(max_length=20)
    comment=models.CharField(max_length=2000)
    class Meta:
        db_table="feedback"

class dth_payment_details(models.Model):
  
    pack=[
        ('for 1 month-RS 250.','for 1 month-RS 250.'),
        ('for 3 month-RS 650.','for 3 month-RS 650.'),
        ('for 6 month-RS 950.','for 6 month-RS 950.'),
        ('for 1 year-RS 1650.','for 1 year-RS 1650.'),
    ]
    Pack      = models.CharField(choices=pack,max_length=97)
    amount    =models.IntegerField()
    class Meta:
        db_table='dth'


class recharge_payment_his(models.Model):
  
    pack=[
        ('549=UL Call 2GB/D,56D','549=UL Call 2GB/D,56D'),
        ('65=4GB,existingpack','65=4GB,existingpack.'),
        ('479=UL Call 1.5GB/D,56D.','479=UL Call 1.5GB/D,56D.'),
        ('359=UL Call 2GB/D,28D.','359=UL Call 2GB/D,28D.'),
        ('2999=UL Call 2GB/D,1Y','2999=UL Call 2GB/D,1Y'),
        ('839=UL Call 2GB/D,84D','839=UL Call 2GB/D,84D'),
        ('299=UL Call 2GB/D,28D','299=UL Call 2GB/D,28D'),
        ('719=UL Call 1.5GB/D,84D','719=UL Call 1.5GB/D,84D'),
    ]
    Pack      = models.CharField(choices=pack,max_length=97)
    amount    =models.IntegerField()
    class Meta:
        db_table='rec'


class h_rent(models.Model):
    bank=[
        ('sbi','sbi'),
        ('iob','iob'),
    ]
    Bank       = models.CharField(choices=bank,max_length=7)
    bank_acc     = models.BigIntegerField()
    bank_ifsc   = models.IntegerField()
    acc_name     = models.CharField(max_length=20)
    ph_no          = models.BigIntegerField()
    class Meta:
        db_table='house_rent'

class s_rent(models.Model):
    bank=[
        ('sbi','sbi'),
        ('iob','iob'),
    ]
    Bank       = models.CharField(choices=bank,max_length=7)
    bank_acc     = models.BigIntegerField()
    bank_ifsc   = models.IntegerField()
    acc_name     =models.CharField(max_length=20)
    ph_no          = models.BigIntegerField()
    class Meta:
        db_table='shop_rent'

class s_main(models.Model):
    bank=[
        ('sbi','sbi'),
        ('iob','iob'),
    ]
    Bank       = models.CharField(choices=bank,max_length=7)
    bank_acc     = models.BigIntegerField()
    bank_ifsc   = models.IntegerField()
    acc_name     =models.CharField(max_length=20) 
    ph_no          = models.BigIntegerField()
    class Meta:
        db_table='social_maintenance'

class EB_history(models.Model):
    State=[
        ('TamilNadu','TamilNadu'),
        ('Kerala','Kerala'),
        ('Karnataka','Karnataka'),
        ('AndhraPradesh','AndhraPradesh'),
    ]
    state      = models.CharField(choices=State,max_length=17)
    EB    = models.BigIntegerField()
    class meta:
        db_table="EB_ALL"
