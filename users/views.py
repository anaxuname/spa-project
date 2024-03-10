from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    """
    Простой ViewSet-класс для вывода списка пользователей и информации по одному объекту
    """

    def list(self, request):
        # Метод для вывода списка пользователей с определением выборки из базы и указанием сериализатора
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Метод для вывода информации по пользователю с определением выборки из базы и указанием сериализатора
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
