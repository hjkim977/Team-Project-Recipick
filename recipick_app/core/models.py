import uuid
import os

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def profile_image_file_path(instance, filename):
    """새로운 이미지에대한 이미지 경로 생성"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads', 'user', filename)


class UserManager(BaseUserManager):

    def create_user(self, id, email, password, **extra_fields):
        if not id:
            raise ValueError('ID를 반드시 입력해주세요.')
        if not email:
            raise ValueError('이메일을 반드시 입력해주세요.')
        if not password:
            raise ValueError('비밀번호를 반드시 입력해주세요.')

        from .models import Level
        default_level = Level.objects.get_or_create(name='초보요리사')[0]
        extra_fields.setdefault('level', default_level)

        user = self.model(
                        id=id,
                        email=self.normalize_email(email),
                        **extra_fields
        )
        user.set_password(password)  # 비밀번호를 암호화하여 저장
        user.save(using=self._db)

        return user

    def create_superuser(self, id, email, password):
        user = self.create_user(id, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    level = models.ForeignKey(
            'Level',
            on_delete=models.SET_NULL,
            blank=True,
            null=True
    )
    profile_image = models.ImageField(
            upload_to=profile_image_file_path,
            blank=True,
            null=True
    )
    loc = models.FloatField(null=True, blank=True)

    objects = UserManager()
    # User 모델이 UserManager모델의 기능을 사용하도록 지정

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['email']


class Level(models.Model):
    name = models.CharField(max_length=20, unique=True, default='초보요리사')

    def __str__(self):
        return self.name
