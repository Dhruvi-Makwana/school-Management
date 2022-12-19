# Generated by Django 2.2.16 on 2022-11-17 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20221027_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='standards',
            field=models.ManyToManyField(help_text='every standard subject list to be stored', related_name='standard', to='school.Standards'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_teacher',
            field=models.ManyToManyField(help_text='each subject faculty name to be stored', related_name='subject', to=settings.AUTH_USER_MODEL),
        ),
    ]
