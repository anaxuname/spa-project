# from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateView(generics.CreateAPIView):
    pass


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateView(generics.UpdateAPIView):
    pass


class HabitDeleteView(generics.DestroyAPIView):
    pass


class HabitRetrieveView(generics.RetrieveAPIView):
    pass
