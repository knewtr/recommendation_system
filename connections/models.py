from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Connection(models.Model):
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Рейтинг",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    class Meta:
        verbose_name = "Связь"
        verbose_name_plural = "Связи"
        unique_together = (("user", "book"),)
        indexes = [models.Index(fields=["user", "book"])]

    def __str__(self):
        return f"Рейтинг книги - {self.rating}"


# здесь должна быть функция обновления/сохранения рейтинга
