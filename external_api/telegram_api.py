from spa_project import settings
import requests


class TelegramAPI:
    def __init__(self):
        self.URL = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}"

    def send_message(self, chat_id, text):
        requests.post(
            url=f"{self.URL}/sendMessage",
            data={"chat_id": chat_id, "text": text},
            timeout=15,
        )
