from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from users.models import User


class TestHabits(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            password="testpassword",
            email="testemail@ex.com",
            full_name="Test User",
            phone_number="1234567890",
            chat_id="1234567890",
        )
        self.user.set_password("testpassword")
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.habit = Habit.objects.create(
            user=self.user,
            place="outside",
            is_enjoyable=True,
            time_for_habit="12:00:00",
            action="hand charger",
            reward="fruit",
            is_public=True,
            continuance=120,
        )

    def test_get_habit_list(self):
        response = self.client.get(reverse("habits:public-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "place": "outside",
                        "is_enjoyable": True,
                        "time_for_habit": "12:00:00",
                        "action": "hand charger",
                        "reward": "fruit",
                        "associated_habit": None,
                        "periodicity": 1,
                        "continuance": 120,
                    }
                ],
            },
        )

    def test_habit_delete(self):
        response = self.client.delete(reverse("habits:delete", args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_create(self):
        data = {
            "place": "at home",
            "time_for_habit": "06:00:00",
            "action": "wake up",
            "periodicity": 7,
            "reward": "coffee",
            "continuance": 10,
        }
        response = self.client.post(reverse("habits:create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            {
                "place": "at home",
                "time_for_habit": "06:00:00",
                "action": "wake up",
                "is_enjoyable": False,
                "associated_habit": None,
                "periodicity": 7,
                "reward": "coffee",
                "continuance": 10,
            },
        )

    def test_get_habit_detail(self):
        response = self.client.get(reverse("habits:retrieve", args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "place": "outside",
            "time_for_habit": "12:00:00",
            "action": "hand charger",
            "is_enjoyable": True,
            "associated_habit": None,
            "periodicity": 1,
            "reward": "fruit",
            "continuance": 120,
        }
        self.assertEqual(response.data, expected_data)

    def test_update_habit(self):
        data = {
            "place": "at home",
            "time_for_habit": "07:00:00",
            "action": "drink water",
            "is_enjoyable": True,
            "periodicity": 7,
            "reward": "fruit",
            "continuance": 20,
        }
        response = self.client.put(reverse("habits:update", args=[self.habit.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "place": "at home",
                "time_for_habit": "07:00:00",
                "action": "drink water",
                "is_enjoyable": True,
                "associated_habit": None,
                "periodicity": 7,
                "reward": "fruit",
                "continuance": 20,
            },
        )
