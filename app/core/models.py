"""
Database models
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user manager
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a new user
        """
        if not email:
            raise ValueError('Users must have an email address')
        # self.normalize_email is a helper function that comes with the
        # BaseUserManager that will normalize the second half of the email
        # address to the lower case.
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # self.model is a helper function that comes with the BaseUserManager
        # that will create a new user model.
        user.set_password(password)
        user.save(using=self._db)
        # self._db is a helper function that comes with the BaseUserManager
        # that will allow you to support multiple databases.
        return user

    def create_superuser(self, email, password):
        """
        Create and save a new superuser
        """
        user = self.create_user(email, password)
        # self.create_user is a function that we created above.
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        # self._db is a helper function that comes with the BaseUserManager
        # that will allow you to support multiple databases.
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system
    """

    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # required for custom user
    is_staff = models.BooleanField(default=False)  # required for custom user
    # is_staff is a field that determines whether the user is a staff user.

    USERNAME_FIELD = 'email'  # required for custom user model
