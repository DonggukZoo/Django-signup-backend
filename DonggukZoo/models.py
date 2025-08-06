# DonggukZoo/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# 커스텀 매니저 (사용자 생성 로직을 관리)
class CustomUserManager(BaseUserManager):
    def create_user(self, student_id, password=None, **extra_fields):
        if not student_id:
            raise ValueError(_('The Student ID must be set'))

        user = self.model(
            student_id=student_id,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('usertype', 'lender')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(student_id, password, **extra_fields)


# 커스텀 사용자 모델
class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        # '대여하는 사람'을 '대여해주는 사람'으로 수정
        ('lender', '대여해주는 사람'),
        ('borrower', '대여하려는 사람'),
    )

    student_id = models.IntegerField(unique=True, verbose_name='학번')
    
    username = models.CharField(max_length=150, verbose_name='사용자 이름')
    usertype = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='borrower',
        verbose_name='유저 타입'
    )
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'donggukzoo_customuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'