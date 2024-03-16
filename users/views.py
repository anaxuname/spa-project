from users.models import User
from users.serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet-класс для вывода списка пользователей и информации по одному объекту
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
