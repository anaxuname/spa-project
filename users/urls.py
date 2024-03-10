from users.apps import UsersConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path(" ", include(router.urls)),
] + router.urls
