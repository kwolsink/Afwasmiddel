from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class AfwasmiddelUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        """
        Creates a regular user
        :param email: the email of the user
        :param username: the username of the user
        :param password: the password of the user
        :return: the user instance
        """
        if not email:
            raise ValueError('Email must be set!')
        if not username:
            raise ValueError('Username must be set!')
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """
        Creates a super user
        :param email: the email of the user
        :param username: the username of the user
        :param password: the password of the user
        :return: the super user instance
        """
        if not password:
            raise ValueError('A valid password must be set!')
        super_user = self.create_user(email=email, username=username, password=password)
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save(using=self._db)

        return super_user


class AfwasmiddelUser(AbstractUser):
    """
    The user model in afwasmiddel. We user email the username field instead of the normal username field.
    """
    email = models.EmailField(verbose_name='email', unique=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS are the fields that are required when create_super_user is called, it isn't used elsewhere.
    REQUIRED_FIELDS = ['username']
    # The user manager
    objects = AfwasmiddelUserManager()

    def __str__(self):
        return self.email


