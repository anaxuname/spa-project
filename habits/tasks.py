from datetime import datetime
from habits.models import Habit
from external_api.telegram_api import TelegramAPI
from celery import shared_task


@shared_task
def send_messages():
    t_api = TelegramAPI()
    now = datetime.now().strftime("%H:%M:00")
    habits = Habit.objects.filter(
        time_for_habit=now,
        periodicity__gt=0,
    )
    for habit in habits:
        t_api.send_message(
            habit.user.chat_id,
            f"я буду {habit.action} в {habit.time_for_habit} в {habit.place}",
        )
