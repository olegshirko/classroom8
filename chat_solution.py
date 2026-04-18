"""
Эталонное решение.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
HISTORY_LIMIT = 20  # сколько сообщений держим в контексте

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Ты дружелюбный помощник для изучения Python. "
        "Объясняй просто, приводи короткие примеры кода. "
        "Отвечай на русском."
    ),
}


def send_message(messages: list[dict]) -> str:
    body = {
        "model": MODEL,
        "messages": messages,
    }
    response = requests.post(API_URL, headers=HEADERS, json=body, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def main():
    print("Чат с DeepSeek. Введите 'exit' для выхода.\n")

    history = []

    while True:
        try:
            user_input = input("Вы: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nПока!")
            break

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Пока!")
            break

        # Validate and sanitize input to avoid encoding issues
        try:
            user_input.encode("utf-8").decode("utf-8")
        except UnicodeError:
            print("[Ошибка]: введённый текст содержит недопустимые символы.")
            continue

        history.append({"role": "user", "content": user_input})

        try:
            # system-сообщение всегда первое, история ограничена
            messages = [SYSTEM_PROMPT] + history[-HISTORY_LIMIT:]
            reply = send_message(messages)
        except requests.HTTPError as e:
            print(f"[Ошибка API]: {e.response.status_code} — {e.response.text}")
            history.pop()  # убираем последнее сообщение, раз не отправили
            continue
        except requests.RequestException as e:
            print(f"[Сетевая ошибка]: {e}")
            history.pop()
            continue

        history.append({"role": "assistant", "content": reply})

        print(f"\nDeepSeek: {reply}\n")

        # Бонус: сохраняем лог
        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"Вы: {user_input}\n")
            f.write(f"DeepSeek: {reply}\n")
            f.write("-" * 40 + "\n")


if __name__ == "__main__":
    main()
