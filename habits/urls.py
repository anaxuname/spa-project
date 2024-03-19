from habits.apps import HabitsConfig
from django.urls import path

from habits.views import (
    HabitCreateView,
    HabitDeleteView,
    HabitListView,
    HabitRetrieveView,
    HabitUpdateView,
    HabitsListViewForUser,
)


app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListView.as_view(), name="public-list"),
    path("list/", HabitsListViewForUser.as_view(), name="user-list"),
    path("create/", HabitCreateView.as_view(), name="create"),
    path("update/<int:pk>/", HabitUpdateView.as_view(), name="update"),
    path("retrieve/<int:pk>/", HabitRetrieveView.as_view(), name="retrieve"),
    path("delete/<int:pk>/", HabitDeleteView.as_view(), name="delete"),
]
