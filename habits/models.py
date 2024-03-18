from django.db import models

from spa_project import settings


class Habit(models.Model):
    """
    Habit - модель привычки
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name="Place")
    time_for_habit = models.TimeField(verbose_name="Habit time")
    action = models.CharField(max_length=100, verbose_name="Action")
    is_enjoyable = models.BooleanField(default=False, verbose_name="Is enjoyable")
    associated_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Associated habit"
    )
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Periodicity", help_text="Days in a week")
    reward = models.CharField(max_length=100, blank=True, null=True, verbose_name="Reward for action")
    continuance = models.IntegerField(verbose_name="Continuance habit in seconds")
    is_public = models.BooleanField(default=False, verbose_name="Is public")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
