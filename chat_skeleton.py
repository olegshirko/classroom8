"""
Практика: HTTP-клиент для чата с AI
====================================
Цель: написать консольный чат, который общается с DeepSeek через API.

Запуск:
    pip install requests
    python chat.py

Документация DeepSeek API:
    https://platform.deepseek.com/api-docs
    (совместим с OpenAI - формат запросов одинаковый)
"""

import requests
import os
from dotenv import load_dotenv

# --- Настройки ---
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


# ---------------------------------------------------------------
# ЗАДАНИЕ 1: Функция отправки одного сообщения
# ---------------------------------------------------------------
# Принимает список сообщений (история), возвращает ответ модели (строку).
#
# Что отправляем (тело POST-запроса):
# {
#     "model": "deepseek-chat",
#     "messages": [
#         {"role": "user", "content": "Привет!"}
#     ]
# }
#
# Что приходит в ответ (response.json()):
# {
#     "choices": [
#         {
#             "message": {
#                 "role": "assistant",
#                 "content": "Привет! Чем могу помочь?"
#             }
#         }
#     ]
# }
#
# Нам нужно: response.json()["choices"][0]["message"]["content"]

def send_message(messages: list[dict]) -> str:
    """Отправить историю сообщений в API, вернуть текст ответа."""

    # Шаг 1: сформируй тело запроса
    body = {
        # TODO: добавь "model" и "messages"
    }

    # Шаг 2: отправь POST-запрос
    # response = requests.post(API_URL, headers=HEADERS, json=body, timeout=30)

    # Шаг 3: проверь что запрос успешный (бросит исключение если 4xx/5xx)
    # response.raise_for_status()

    # Шаг 4: достань текст ответа и верни его
    # Подсказка: response.json()["choices"][0]["message"]["content"]
    return ""


# ---------------------------------------------------------------
# ЗАДАНИЕ 2: Основной цикл чата
# ---------------------------------------------------------------
# История - это обычный список словарей.
# Каждое сообщение: {"role": "user" или "assistant", "content": "текст"}
#
# Пример как выглядит history после двух реплик:
# [
#     {"role": "user",      "content": "Что такое список?"},
#     {"role": "assistant", "content": "Список - это..."},
#     {"role": "user",      "content": "А словарь?"},
# ]
#
# Именно этот список ты передаёшь в send_message() -
# модель видит всю историю и отвечает с учётом контекста.
#
# Алгоритм:
# 1. Создай пустой список history = []
# 2. В бесконечном цикле:
#    а) user_input = input("Вы: ")
#    б) Если user_input == "exit" - break
#    в) Добавь {"role": "user", "content": user_input} в history
#    г) reply = send_message(history)
#    д) Добавь {"role": "assistant", "content": reply} в history
#    е) print(f"DeepSeek: {reply}")

def main():
    print("Чат с DeepSeek. Введите 'exit' для выхода.\n")

    history = []  # список сообщений - история диалога

    while True:
        # TODO: реализуй цикл диалога по алгоритму выше
        pass


# ---------------------------------------------------------------
# БОНУС (если успеваешь):
# ---------------------------------------------------------------
# 1. Добавь system-сообщение ПЕРЕД history при отправке:
#    system = {"role": "system", "content": "Ты помощник для изучения Python. Отвечай кратко."}
#    messages = [system] + history
#
# 2. Ограничь историю последними 10 сообщениями (иначе растёт бесконечно):
#    messages = [system] + history[-10:]
#
# 3. Сохраняй диалог в файл chat_log.txt после каждого ответа.
#
# 4. Обработай ошибки через try/except requests.RequestException


if __name__ == "__main__":
    main()
