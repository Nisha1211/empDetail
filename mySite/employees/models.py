from django.db import models


# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', "Female")]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email_id = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=13)
    employee_gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    employee_job = models.ManyToManyField('AvailableJobs', blank=True)
    employee_address = models.TextField()
    date_of_birth = models.DateField()


class AvailableJobs(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name