from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from books.models import Author, Genre


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должна быть почта")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    name = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
        help_text="Укажите имя",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    favourite_book = models.CharField(
        max_length=150,
        verbose_name="Любимая книга",
        blank=True,
        null=True,
    )
    favourite_author = models.ManyToManyField(
        Author,
        verbose_name="Любимый автор",
        blank=True,
        null=True,
    )
    favourite_genre = models.ManyToManyField(
        Genre,
        verbose_name="Любимый жанр",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
