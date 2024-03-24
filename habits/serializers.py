from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    HabitValidator,
    continuance_validator,
    periodicity_validator,
)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор привычки
    """

    continuance = serializers.IntegerField(validators=[continuance_validator])
    periodicity = serializers.IntegerField(validators=[periodicity_validator])

    def create(self, validated_data):
        return Habit.objects.create(**validated_data)

    class Meta:
        model = Habit
        fields = (
            "place",
            "time_for_habit",
            "action",
            "is_enjoyable",
            "associated_habit",
            "periodicity",
            "reward",
            "continuance",
            "is_public",
        )
        validators = [HabitValidator()]
