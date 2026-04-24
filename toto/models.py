from django.db import models

# Create your models here.
# class details(models.Model):
#     SN=models.AutoField
#     Name=models.CharField(max_length=255)
#     Blood=models.CharField(max_length=20,default="")
#     Date=models.DateField()
    

    
#     def __str__(self):
#         return self.Name

class det(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50 ,default='')
    email=models.CharField(max_length=100 , default='')
    message=models.CharField(max_length=2000 ,default='')
    def __str__(self):
         return self.name
        
# class det(models.Model):
#     id=models.AutoField(primary_key=True)
#     firstname= models.CharField(max_length=200, default='')
#     middlename= models.CharField(max_length=200, default='')
#     lastname= models.CharField(max_length=200, default='')
#     address= models.CharField(max_length=200, default='')
#     bloodgroup= models.CharField(max_length=200, default='')
#     phone= models.PhoneNumberField(_(""))
#     email=models.CharField(max_length=100 , default='')

class receipent(models.Model):
    id=models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=200, default='')
    middlename= models.CharField(max_length=200, default='')
    lastname= models.CharField(max_length=200, default='')
    gender= models.CharField(max_length=200, default='')
    address= models.CharField(max_length=200, default='')
    bloodgroup= models.CharField(max_length=200, default='')
    image=models.FileField(upload_to="toto/image", default='' )
    phone= models.IntegerField(default=0)
    email=models.CharField(max_length=100 , default='')
    def __str__(self):
        return self.firstname
    


class donor(models.Model):
    id=models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=200, default='')
    middlename= models.CharField(max_length=200, default='')
    lastname= models.CharField(max_length=200, default='')
    gender= models.CharField(max_length=200, default='')
    address= models.CharField(max_length=200, default='')
    bloodgroup= models.CharField(max_length=200, default='')
    image=models.FileField(upload_to="toto/image", default='' )
    phone= models.IntegerField(default=0)
    email=models.CharField(max_length=100 , default='')
    password= models.CharField(max_length=200, default='')
    def __str__(self):
       return self.firstname

    

    

    


    