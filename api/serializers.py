from rest_framework.serializers import ModelSerializer

from books.models import Author, Book, Genre
from connections.serializers import ConnectionSerializer
from users.models import User


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "rating"]


class BookDetailedSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "cover",
            "author",
            "genre",
            "publication_date",
            "rating",
            "description",
        ]


class UserSerializer(ModelSerializer):
    connection = ConnectionSerializer(read_only=True, mane=True)
    favourite_genres = GenreSerializer(read_only=True, mane=True)

    class Meta:
        model = User
        fields = ["id", "password", "email", "name", "avatar"]


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
