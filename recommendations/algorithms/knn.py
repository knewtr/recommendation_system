import math

from recommendations.services import create_recommendation

from books.models import Book
from connections.models import Connection
from users.models import User


class KNNeighbour:

    @staticmethod
    def recommendations(user_id, top_n=5):
        ranked_books = list(
            Connection.objects.filter(user=user_id)
            .exclude(rating=None)
            .values_list("book_id", flat=True)
        )
        print(ranked_books)

        neighbours = list(
            Connection.objects.filter(book_id__in=ranked_books, rating__isnull=False)
            .distinct()
            .exclude(user=user_id)
            .values_list("user_id", flat=True)
        )

        distance_list = []
        for n in neighbours:
            total = 0
            for book in ranked_books:
                a = Connection.objects.get(user=user_id, book=book).rating
                if (
                    Connection.objects.filter(user=n, book=book)
                    .exclude(rating=None)
                    .exsist()
                ):
                    b = Connection.objects.get(user=n, book=book).rating
                    total += (a - b) ** 2
            distance = math.sqrt(total)
            distance_list.append({"user": n, "distance": distance})

        sorted_distance_list = sorted(distance_list, key=lambda x: x["distance"])
        sorted_neighbour = list(n["user"] for n in sorted_distance_list)

        k = round(math.sqrt(len(User.objects.all())))
        top_books = (
            Connection.objects.filter(user_id__in=sorted_neighbour[:k], rating__gte=4)
            .exclude(book_id__in=ranked_books)
            .values_list("book_id", flat=True)
            .distinct()
        )

        recommended_books = []
        for book in top_books:
            recommended_books.append(
                {
                    "book_id": book,
                    "avg_rating": Book.objects.get(id=book).average_rating,
                }
            )

        sorted_recommended_books = sorted(
            recommended_books, key=lambda x: x["avg_rating"], reverse=True
        )[:top_n]
        book_id_list = list(x["book_id"] for x in sorted_recommended_books)

        user = User.objects.get(id=user_id)
        recommendation = create_recommendation(user, "knn", book_id_list)

        return list(recommendation.books.all())
