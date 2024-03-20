from typing import Any
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def continuance_validator(continuance):
    """
    Время исполнения привычки не может быть больше 120 секунд
    """
    if continuance > 120:
        raise serializers.ValidationError("Время исполнения привычки не может быть больше 120 секунд")


def periodicity_validator(periodicity):
    """
    Периодичность привычки не может быть больше 7 раз в неделю
    """
    if periodicity > 7:
        raise serializers.ValidationError("Периодичность привычки не может быть реже 1 раза в неделю")


class HabitValidator:
    """
    Проверка на исключения при создании привычки
    """

    def __init__(self, is_enjoyable, associated_habit, reward) -> None:
        self.is_enjoyable = is_enjoyable
        self.associated_habit = associated_habit
        self.reward = reward

    def __call__(self, value) -> Any:
        is_enjoyable = value.get(self.is_enjoyable)
        associated_habit = value.get(self.associated_habit)
        reward = value.get(self.reward)

        if associated_habit and not is_enjoyable:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")
        if is_enjoyable and (associated_habit or reward):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
        if associated_habit and reward:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и вознаграждение")

        if not is_enjoyable and not reward:
            raise ValidationError("У полезной привычки необходимо указать вознаграждение или приятную привычку")
