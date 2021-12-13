from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import MyUserManager
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


# A primitive extension of the standard User table from Django lib
class User(AbstractBaseUser):
    ChoiceRole = (
        ("Admin", "Admin"),
        ("Quality Control", "Quality Control"),
        ("Production", "Production"),
        ("Quality Assurance", "Quality Assurance"),
        ("Store", "Store"),
    )
    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyUserManager()

    role= models.CharField(default='Accounts',max_length=50,choices=ChoiceRole)
    profilepic = models.CharField(blank=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return self.username






