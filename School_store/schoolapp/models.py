from django.db import models

# Create your models here.
class PlaceOrder(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    address = models.TextField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    DEPARTMENT_CHOICES = (
        ('data_science', 'Data Science'),
        ('artificial_intelligence', 'Artificial Intelligence'),
        ('machine_learning', 'Machine Learning'),
        ('BSc_Physics', 'BSc Physics'),
        ('BSc_Chemistry', 'BSc Chemistry'),
        ('BSc_Biology', 'BSc Biology'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
        ('BCom', 'BCom'),
        ('MCom', 'MCom'),
        ('Statitics', 'Statitics'),
        ('History', 'History'),
        ('Economics', 'Economics'),
        ('Political_Science', 'Political Science'),
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    ITEM_CHOICES = (
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('epaper', 'Exam Paper'),
        ('inst_box', 'Instrument Box'),
        ('calculator', 'Calculator'),
    )
    item = models.CharField(max_length=50, choices=ITEM_CHOICES)
    PURPOSE_CHOICES = (
        ('order', 'Place Order'),
        ('return', 'Return Item'),
    )
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    dob = models.DateField()