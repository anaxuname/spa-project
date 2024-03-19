from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import MaterialPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsAuthorOrReadOnly


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        return super().perform_create(serializer)


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialPaginator


class HabitsListViewForUser(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class HabitDeleteView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class HabitRetrieveView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
