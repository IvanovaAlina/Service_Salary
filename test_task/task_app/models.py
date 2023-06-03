from django.db import models
from django.contrib.auth.models import User
import django
from datetime import date

# Create your models here.
class InformSalary(models.Model):
    summ_check = models.DecimalField(max_digits = 100, decimal_places=2)
    date_check = models.DateField(default=date.today())
    date_next_raise = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


class CodeConfirmEmail(models.Model):
    code_verify = models.CharField(max_length = 1000)
    email_for_verify = models.CharField(max_length = 1000)
    date_added = models.DateTimeField(auto_now_add=True)
    flag_verify = models.BooleanField(default = False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
