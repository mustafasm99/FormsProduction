from django.db import models
from django.contrib.auth.models import User
from form.models import Form
from django.core.validators import MaxValueValidator
# Create your models here.


class Student(models.Model):
    user            = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=20)
    mid_name        = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    phone_number1   = models.CharField(max_length=15)
    phone_number2   = models.CharField(max_length=15)
    location        = models.CharField(max_length=20)
    cource          = models.ManyToManyField('Cource')
    cource_limet    = models.IntegerField()
    Form            = models.ForeignKey(Form , on_delete=models.CASCADE , null=True , blank=True)
    editbal         = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+" "+self.mid_name+" "+self.last_name
    

class Cource(models.Model):
    name           = models.CharField(max_length=20)
    Teacher        = models.ForeignKey("Teacher",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Teacher(models.Model):
    name            = models.CharField(max_length=20)
    image           = models.ImageField(upload_to="techer_img")
    col             = models.IntegerField(validators=[MaxValueValidator(100)])
    row             = models.IntegerField(validators=[MaxValueValidator(100)])
    form            = models.ForeignKey(Form , on_delete=models.SET_NULL , null=True , blank=True)
    filter          = models.ForeignKey('filters' , on_delete=models.SET_NULL , null=True , blank=True)
    
    def __str__(self):
        return self.name
    
    def get_all_cources(self,json=False):
        if json:
            return Cource.objects.filter(Teacher=self).values().all()
        return Cource.objects.filter(Teacher=self).all()

class filters(models.Model):
    name             = models.CharField(max_length=50)
    form             = models.ForeignKey(Form , on_delete=models.SET_NULL, null=True , blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_all_courses(self):
        return Teacher.objects.filter(
            form   = self.form,
            filter = self
        ).all()