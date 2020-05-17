from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather', 'RatherNotSay'),
)

CELLPHONE_CHOICE = (
    ('91','+91'),
    ('92','+92'),
    ('93','+93'),
    ('94','+94'),
    ('95','+95'),
    ('96','+96'),
)

LOOKING_CHOICE = (
    ('Just Information', 'Just Information'),
    ('Treatment Details', 'Treatment Details'),
)
class Registration(models.Model):
    mes_id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email = models.EmailField(default="null")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='male')
    selphone=models.CharField(max_length=10, choices=CELLPHONE_CHOICE, default='91')
    contactnumber = models.CharField(max_length=10, default="null")
    password=models.CharField(max_length=20,default="null")
    cpassword = models.CharField(max_length=20,default="null")
    address = models.CharField(max_length=20, default="null")


    def __str__(self):
        return self.fname


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200,default="null")
    message = models.CharField(max_length=2000, default="null")

    def __str__(self):
        return self.name

class MedicineOrdered(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Combiflam = models.IntegerField(default=0)
    Paracetamol = models.IntegerField(default=0)
    Cofsils = models.IntegerField(default=0)
    DigeneTablet = models.IntegerField(default=0)
    DigeneGel = models.IntegerField(default=0)
    Hajmola = models.IntegerField(default=0)
    Seacod = models.IntegerField(default=0)
    Shelcal = models.IntegerField(default=0)
    Crocin = models.IntegerField(default=0)
    Lubrifresh = models.IntegerField(default=0)
    Dettol = models.IntegerField(default=0)
    Ashwagandha = models.IntegerField(default=0)
    Moov = models.IntegerField(default=0)
    Zandu = models.IntegerField(default=0)
    Vicks = models.IntegerField(default=0)
    Chyawanprash = models.IntegerField(default=0)
    totalSum = models.BigIntegerField(default=0)
   
    def __str__(self):
        return str(self.user)

class Askdoctor(models.Model):
        question = models.CharField(max_length=20)
        looking = models.CharField(max_length=20,choices=LOOKING_CHOICE, default='information')
        email = models.EmailField(default="null")
        selphone = models.CharField(max_length=10, choices=CELLPHONE_CHOICE, default='91')
        contactnumber = models.CharField(max_length=10, default="null")

        def __str__(self):
            return self.email

class Contactlogin(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200, default="null")
    message = models.CharField(max_length=2000, default="null")

    def __str__(self):
            return self.name

# class Cart(models.Model):
#     cart_item=models.CharField(max_length=100)
    
        
