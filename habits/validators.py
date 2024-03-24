from typing import Any
from rest_framework import serializers


def continuance_validator(continuance):
    """
    Время исполнения привычки не может быть больше 120 секунд
    """
    if continuance > 120:
        raise serializers.ValidationError(
            "Время исполнения привычки не может быть больше 120 секунд"
        )


def periodicity_validator(periodicity):
    """
    Периодичность привычки не может быть больше 7 раз в неделю
    """
    if periodicity > 7:
        raise serializers.ValidationError(
            "Периодичность привычки не может быть реже 1 раза в неделю"
        )


class HabitValidator:
    """
    Проверка на исключения при создании привычки
    """

    def __call__(self, value) -> Any:
        is_enjoyable = value.get("is_enjoyable")
        associated_habit = value.get("associated_habit")
        reward = value.get("reward")

        if associated_habit and not associated_habit.is_enjoyable:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки"
            )
        if is_enjoyable and (associated_habit or reward):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )
        if associated_habit and reward:
            raise serializers.ValidationError(
                "Нельзя одновременно выбрать связанную привычку и вознаграждение"
            )
