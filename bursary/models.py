from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CONSTITUENCY = (
        ('Serene Stays','Serene Stays'),
        ('Haven Hills', 'Haven Hills'),
        ('Tranquil Pines', 'Tranquil Pines'),
        ('Sunset Retreat', 'Sunset Retreat'),
    )
    WARD = (
        ('Lakeside Haven', 'Lakeside Haven'),
        ('Whispering Pines BnB', 'Whispering Pines BnB'),
        ('Cozy Corner BnB', 'Cozy Corner BnB'),
        ('Hilltop Hideaway', 'Hilltop Hideaway'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    id_card = models.ImageField(default="default_id_card.png", null=False, blank=True)
    institution = models.CharField(max_length=200, null=True)
    fees_structure = models.FileField(default="default_fees_structure.pdf", null=False, blank=True)
    year_of_study = models.CharField(max_length=200, null=True)
    Constituency = models.CharField(max_length=200, null=False, choices=CONSTITUENCY, default='Kibwezi West')
    ward = models.CharField(max_length=200, null=False, choices=WARD, default='None')

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Student"



class Bursary(models.Model):
    CATEGORY = (
        ('Studio', 'Studio'),
        ('Private Room', 'Private Room'),
        ('Villa', 'Villa'),
    )
    name = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    batchNumber = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Applications(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Booking in Progress', 'Booking in Progress'),
        ('Confirmed', 'Confirmed'),
    )
    ApplyAmount = (
        ('KSH 5000.00', 'KSH 5000.00'),
        ('KSH 6500.00', 'KSH 6500.00'),
        ('KSH 8000.00', 'KSH 8000.00'),
        ('KSH 10000.00', 'KSH 10000.00'),
    )

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name="applications")
    bursary = models.ForeignKey(Bursary, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    applyAmount = models.CharField(max_length=200, null=True, choices=ApplyAmount)


def __str__(self):
    if self.bursary:
        return self.bursary.name
    return "No Bursary"

