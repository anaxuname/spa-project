from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet-класс для вывода списка пользователей и информации по одному объекту
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == "list" or self.action == "retrieve" or self.action == "delete":
            permission_classes = [IsAdmin]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [IsAdmin | IsAuthenticated]
        return [permission() for permission in permission_classes]
