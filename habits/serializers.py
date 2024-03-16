from rest_framework import serializers

from habits.models import Habit
from habits.validators import continiance_validator, periodicity_validator


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор привычки
    """

    continuance = serializers.IntegerField(validators=[continiance_validator])
    periodicity = serializers.IntegerField(validators=[periodicity_validator])

    class Meta:
        model = Habit
        fields = "__all__"
