from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.utils.translation import ugettext_lazy as _
from organization_management.models import Organization

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')
        username = self.model.normalize_username(username)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(
            username,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        null=False,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    objects = MyUserManager()
    organization = models.ForeignKey("organization_management.Organization", null=True, blank=True, related_name="users", on_delete=models.CASCADE)


class Account(User):
    organizations = models.ManyToManyField(Organization)