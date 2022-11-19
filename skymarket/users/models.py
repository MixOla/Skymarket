from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = ((USER, 'Пользователь'), (ADMIN, 'Администратор'))


class User(AbstractBaseUser):
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # переопределим менеджер модели пользователя

    objects = UserManager()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(verbose_name="email address", unique=True)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.USER, max_length=13)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
