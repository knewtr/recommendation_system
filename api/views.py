from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet

from api.serializers import BookDetailedSerializer, BookSerializer, UserSerializer
from books.models import Book
from connections.models import Connection
from connections.serializers import ConnectionSerializer
from users.models import User


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get("password"))
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(ModelViewSet):

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailedSerializer
        return BookSerializer


class ConnectionViewSet(ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Connection.objects.all()
        return Connection.objects.filter(user=user)

    def create(self, serializer):
        serializer.save(user=self.request.user)


class RecommendationAPIView(APIView):

    def get(self, request):
        pr_rec = PageRank.recommendations(request.user.id, 5)
        knn_rec = KNN.recommendations(request.user.id, 5)
        serialized_data = {
            "pr_rec": FilmSerializer(pr_rec, many=True).data,
            "knn_rec": FilmSerializer(knn_rec, many=True).data,
        }

        return Response(serialized_data)
