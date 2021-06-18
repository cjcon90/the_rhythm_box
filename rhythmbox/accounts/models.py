from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField



class MyAccountManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, newsletter, password=None
    ):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a First Name")
        if not last_name:
            raise ValueError("Users must have a Last Name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            newsletter=newsletter,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, newsletter, last_name, password
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            newsletter=newsletter,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(
        verbose_name="first name", max_length=30, unique=False
    )
    last_name = models.CharField(
        verbose_name="last name", max_length=30, unique=False
    )
    newsletter = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "newsletter"]

    objects = MyAccountManager()

    def clean(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Address(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="address")
    street_address_1 = models.CharField(max_length=80)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    country = CountryField(blank=False, default="IE")
    phone_number = models.CharField(max_length=20)