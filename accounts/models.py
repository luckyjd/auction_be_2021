from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

ITEM_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
            ('P','Portion'),
            )


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    size = models.CharField(choices=ITEM_SIZES, max_length=1, default='M')
    pass
