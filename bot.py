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


def send_notification():
    pr_number = os.getenv("PR_NUMBER", "-")
    pr_title = os.getenv("PR_TITLE", "Тестовый запуск")
    pr_url = os.getenv("PR_URL", "-")
    pr_author = os.getenv("PR_AUTHOR", "неизвестен")
    source_branch = os.getenv("PR_SOURCE_BRANCH", "-")
    target_branch = os.getenv("PR_TARGET_BRANCH", "-")
    job_status = os.getenv("JOB_STATUS", "unknown").upper()
    run_id = os.getenv("RUN_ID", "локальный")

    status = "Успешно" if job_status == "SUCCESS" else "Ошибка"
    status_color = "success" if job_status == "SUCCESS" else "danger"

    message = (
        f"*Новый Pull Request #{pr_number}*\n\n"
        f"**{pr_title}**\n"
        f"Автор: @{pr_author}\n"
        f"Ветка: `{source_branch}` -> `{target_branch}`\n"
        f"Ссылка: {pr_url}\n\n"
        f"Статус проверки: **{status}**\n"
        f"Run ID: {run_id}\n"
        f"Время: {os.popen('date').read().strip()}"
    )

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
    success = send_notification()
    if not success:
        sys.exit(1)
