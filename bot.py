import os
import sys
import telebot


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN:
    print("ОШИБКА: TELEGRAM_BOT_TOKEN не задан")
    sys.exit(1)

if not CHAT_ID:
    print("ОШИБКА: TELEGRAM_CHAT_ID не задан")
    sys.exit(1)


bot = telebot.TeleBot(TOKEN)


def send_notification(message: str):
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="Markdown"
        )
        print("ПОБЕДА: сообщение отправлено")
        print(f"Текст:\n{message}")
        return True
    except Exception as e:
        print(f"НЕ ПОБЕДА: {str(e)}")
        return False


if __name__ == "__main__":
    test_message = (
        "*Тестовое уведомление из GitHub Actions*\n\n"
        "Pipeline успешно запустился\n"
        f"Токен: {'присутствует' if TOKEN else 'ОТСУТСТВУЕТ'}\n"
        f"Chat ID: {CHAT_ID}"
    )

    success = send_notification(test_message)

    if not success:
        sys.exit(1)
