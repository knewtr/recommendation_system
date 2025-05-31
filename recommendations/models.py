from django.db import models


class Recommendation(models.Model):
    METHODS = [
        ("knn", "k-nearest neighbour"),
        ("pagerank", "PageRank"),
    ]
    user = models.ForeignKey(
        "users.User",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        "books.Book",
        verbose_name="Книга",
        on_delete=models.CASCADE,
    )
    method = models.CharField(
        choices=METHODS,
        verbose_name="Метод",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "рекомендация"
        verbose_name_plural = "рекомендации"
        ordering = ["id"]

    def __str__(self):
        return f"Рекомендация для {self.user.email}, выполненная методом {self.method} {self.created_at}"
