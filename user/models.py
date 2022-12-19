from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
# from school.models import Standards
# from django.utils.translation import ugettext_lazy as _


FEMALE = "female"
MALE = "male"
GENDER = (
    (MALE, 'male'),
    (FEMALE, 'female')

)
STUDENT = "student"
FACULTY = "faculty"
PRINCIPAL = 'principal'

USER_CHOICES = ((STUDENT, 'student'), (FACULTY, 'faculty'), (PRINCIPAL, 'principal'))


class User(AbstractUser):
    """This model includes all the information related to user
      and user must be one"""
    mobile_number = models.CharField(max_length=10, help_text='phone_no should be added')
    birth_date = models.DateField(null=True, blank=True, help_text='birth date is stored')
    gender = models.CharField(choices=GENDER, blank=True, max_length=30)
    user_type = models.CharField(default=FACULTY, choices=USER_CHOICES, max_length=20)
    parent_name = models.CharField(help_text='enter student parent name', null=True, blank=True, max_length=50)

    def __str__(self):
        return f'{self.username}'
