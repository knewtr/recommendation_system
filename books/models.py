from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")
    description = models.TextField(verbose_name="Описание жанра")

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя автора")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия автора")
    birth_date = models.DateField(verbose_name="Дата рождения")
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        verbose_name="Книга",
        blank=True,
        null=True,
        related_name="books",
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="Жанр",
        blank=True,
        null=True,
        related_name="authors",
    )

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"
        ordering = ["last_name"]


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги")
    cover = models.ImageField(
        upload_to="book_cover",
        blank=True,
        null=True,
        verbose_name="Обложка книги",
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="Жанр",
        blank=True,
        null=True,
        related_name="books",
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        blank=True,
        null=True,
        related_name="authors",
    )
    publication_date = models.DateField(
        verbose_name="Дата публикации",
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"
