from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=128, unique=True)
    is_full_info = models.BooleanField(default=0)

    user_type = models.BooleanField(default=0)   # 0 = individual , 1 = company

    # with user_type = 0
    gender = models.BooleanField(default=0, blank=True, null=True)  # 0 = male , 1 = female
    dob = models.DateField(blank=True, null=True)
    user_city = models.CharField(max_length=128, blank=True, null=True)
    user_district = models.CharField(max_length=128, blank=True, null=True)
    user_wards = models.CharField(max_length=128, blank=True, null=True)
    user_street = models.CharField(max_length=255, blank=True, null=True)
    user_id_card = models.CharField(max_length=128, blank=True, null=True)
    user_id_card_date = models.DateField(blank=True, null=True)
    user_id_card_place = models.CharField(max_length=255, blank=True, null=True)
    user_id_card_image_front = models.FileField(upload_to='user/individual/', blank=True, null=True)
    user_id_card_image_back = models.FileField(upload_to='user/individual/', blank=True, null=True)
    user_bank_no = models.CharField(max_length=128, blank=True, null=True)
    user_bank_name = models.CharField(max_length=128, blank=True, null=True)
    user_bank_branch = models.CharField(max_length=128, blank=True, null=True)
    user_bank_user_name = models.CharField(max_length=128, blank=True, null=True)

    # with user_type = 1
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_business_registration_no = models.CharField(max_length=128, blank=True, null=True)
    company_business_registration_no_date = models.DateField(blank=True, null=True)
    company_business_registration_no_place = models.CharField(max_length=255, blank=True, null=True)
    company_tax_code = models.CharField(max_length=128, blank=True, null=True)
    company_phone = models.CharField(max_length=128, blank=True, null=True)
    company_email = models.CharField(max_length=128, blank=True, null=True)
    company_city = models.CharField(max_length=128, blank=True, null=True)
    company_district = models.CharField(max_length=128, blank=True, null=True)
    company_wards = models.CharField(max_length=128, blank=True, null=True)
    company_street = models.CharField(max_length=255, blank=True, null=True)
    company_represent_surname = models.CharField(max_length=128, blank=True, null=True)
    company_represent_name = models.CharField(max_length=128, blank=True, null=True)
    company_represent_position = models.CharField(max_length=128, blank=True, null=True)
    company_represent_phone = models.CharField(max_length=128, blank=True, null=True)
    company_represent_email = models.CharField(max_length=128, blank=True, null=True)
    company_represent_gender = models.CharField(max_length=128, blank=True, null=True)
    company_represent_dob = models.DateField(blank=True, null=True)
    company_represent_id_card = models.CharField(max_length=128, blank=True, null=True)
    company_represent_id_card_date = models.DateField(blank=True, null=True)
    company_represent_id_card_place = models.CharField(max_length=255, blank=True, null=True)
    company_represent_id_card_image_front = models.FileField(upload_to='user/company/', blank=True, null=True)
    company_represent_id_card_image_back = models.FileField(upload_to='user/company/', blank=True, null=True)
    company_represent_bank_no = models.CharField(max_length=128, blank=True, null=True)
    company_represent_bank_name = models.CharField(max_length=128, blank=True, null=True)
    company_represent_bank_branch = models.CharField(max_length=128, blank=True, null=True)
    company_represent_bank_user_name = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()
