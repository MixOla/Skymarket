from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager, UserRoles

from phonenumber_field.modelfields import PhoneNumberField


# from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'
    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    email = models.EmailField(verbose_name="email address", unique=True, null=False, blank=False)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.USER, max_length=5)
    image = models.ImageField(upload_to='django_media', null=True, blank=True)

    # переопределим менеджер модели пользователя
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
