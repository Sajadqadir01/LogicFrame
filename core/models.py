from encodings.punycode import selective_len
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('ایمیل باید وارد شود')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name='اسم کوچک')
    last_name = models.CharField(max_length=100, verbose_name='فامیلی')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.jpg', verbose_name='پروفایل')
    bio = models.CharField(max_length=100, null=True, blank=True, verbose_name='اطلاعات شخضی')
    phone = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name='شماره تلفون')
    email = models.EmailField(max_length=254, null=False, unique=True, blank=False, verbose_name='ایمیل')
    CURRENCY_CHOICES = (
        ('USD', 'دلار'),
        ('IRT', 'تومان')
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='IRT', verbose_name='واحد پول پیشفزض')
    xp = models.PositiveIntegerField(default=0, verbose_name='امتیاز')
    level = models.PositiveIntegerField(default=1, verbose_name='سظح')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    objects = CustomUserManager()
    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.username}'
    def check_level_up(self):
        new_level = (self.xp // 500) + 1
        if new_level > self.level:
            self.level = new_level
            self.save()
            return True
        return False
