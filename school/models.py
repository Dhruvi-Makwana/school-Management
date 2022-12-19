from django.db import models

# Create your models here.
from django.db import models
from user.models import User
STANDARD_LIST = [
    ('std_5', 'STANDARD_5'),
    ('std_6', 'STANDARD_6'),
    ('std_7', 'STANDARD_7'),
    ('std_8', 'STANDARD_8'),
    ('std_9', 'STANDARD_9'),
    ('std_10', 'STANDARD_10'),
    ('std_11', 'STANDARD_11'),
    ('std_12', 'STANDARD_12'),
]
SUBJECT_LIST = [
    ('gujrati', 'Gujrati'),
    ('english', 'English'),
    ('maths', 'mathematics'),
    ('Science', 'science'),
    ('drawing', 'Drawing'),
    ('hindi', 'Hindi'),
    ('Social_science', 'Social_science'),
]


class SchoolDetails(models.Model):
    name = models.CharField(max_length=30, help_text='info_school name')
    address = models.TextField(help_text='info_school address')
    contact_number = models.CharField(max_length=10, help_text='school registered contact number')
    owner_name = models.CharField(max_length=20, help_text='info_school owner name')


class Standards(models.Model):
    name = models.CharField(max_length=30)
    # student = models.ForeignKey(User, help_text='list of student', on_delete=models.CASCADE, related_name='student',blank=True, null=True)
    class_teacher = models.ForeignKey(User, help_text='class teacher of standerd', blank=True, null=True, related_name='teacher', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Subject(models.Model):
    sub_name = models.CharField(max_length=40, help_text='subject name to be stored')
    subject_teacher = models.ManyToManyField(User, help_text='each subject faculty name to be stored', related_name='subject')
    standards = models.ManyToManyField(Standards, help_text='every standard subject list to be stored', related_name='standard')

    def __str__(self):
        return f'{self.sub_name}'

        # stand = ",".join(str(stan) for stan in self.standards.all())
        # return "{},{}".format(self.sub_name, stand)
        # return f'{self.sub_name} ,{self.standards.all()}'
        # gujrati, < QuerySet[ < Standards: 9, pooja >] >

        # standards = ", ".join(str(stan) for stan in self.standards.all())
        # return "{},{}".format(self.sub_name, standards)
