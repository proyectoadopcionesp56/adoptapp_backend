from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        ADMIN = 'AD', ('Administrador')
        OTORGANTE = 'OT', ('Otorgante')
        ADOPTANTE = 'AP', ('Adoptante')

    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length=30)
    lastname = models.CharField('Lastname', max_length=30)
    IDKind = models.CharField('IDKind', max_length=30)
    IDNumber = models.CharField('IDNumber', max_length=30)
    address = models.CharField('address', max_length=30)
    city = models.CharField('city', max_length=30)
    country = models.CharField('country', max_length=30)
    landline = models.CharField('landline', max_length=30)
    mobilephone = models.CharField('mobilephone', max_length=30)
    jobs = models.CharField('jobs', max_length=30, default="No Aplica")
    company = models.CharField('company', max_length=30, default="No Aplica")
    username = models.CharField('Username', max_length=15, unique=True)
    email = models.EmailField('Email', max_length=100)
    password = models.CharField('Password', max_length=256)
    rol = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.ADOPTANTE,
    )

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'