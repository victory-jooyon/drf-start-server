from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django_mysql.models import JSONField

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        password = extra_fields.get('password')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        user = self._create_user(email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # superuser

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)

    def get_full_name(self):
        return self.name

    def get_username(self):
        return self.email


class UserConfig(models.Model):
    CLIENT_WEB = 'web'
    CLIENT_TYPES = (
        (CLIENT_WEB, 'web'),
    )

    user = models.ForeignKey('User', related_name='configs', on_delete=models.CASCADE)
    client = models.CharField(max_length=10, choices=CLIENT_TYPES)
    key = models.CharField(max_length=64)
    content = JSONField(null=True)
