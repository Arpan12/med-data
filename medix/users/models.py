# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


"""@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})"""

class UserManager(BaseUserManager):

    def create_user(self, username, name, email, mobile, password=None):
        """ Create and save a member"""
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            mobile=mobile,
            is_superuser=False,
            is_active=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, email, mobile, password):
        """ Create and save a superuser."""
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            mobile=mobile,
            is_superuser=True,
            is_active=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Represents a single user."""

    username = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(
        'E Mail address',
        unique=True,
        blank=False,
    )
    mobile = models.CharField(
        'Mobile Number',
        max_length=10,
        blank=False,
        validators=[
            RegexValidator(
                r'^[789]\d{9}$',
                'Invalid mobile number.',
            ),
        ],
    )
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'mobile']

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        """ Required for logging into admin panel."""
        return self.is_superuser

    @property
    def get_short_name():
        return self.name  # noqa

    def get_full_name():
        return '{} <{}>'.format(self.get_short_name(), self.email)  # noqa


