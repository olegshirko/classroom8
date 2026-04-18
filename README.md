# Чат с DeepSeek API

Консольный чат с AI (модель `deepseek-chat`) через HTTP API.

---

## Быстрый старт

### 1. Зависимости

```bash
pip install requests
```

### 2. API-ключ

Заполни файл `.env` в корне проекта:

```
DEEPSEEK_API_KEY=sk-your_key_here
```

Получить ключ → [DeepSeek Platform](https://platform.deepseek.com/api-docs)

### 3. Запуск

**Скелет приложения ** — файл с TODO.

```bash
python3 chat_skeleton.py
```

---

## Структура проекта

```
.
├── chat_skeleton.py          # Шаблон с TODO
├── test_chat.py              # Тесты (unittest + mock)
├── .env                      # API-ключи (НЕ КОММИТИТЬ!)
└── .github/workflows/
    └── tests.yml             # CI: запуск тестов
```

---

## API-ключи и .env

> ⚠️ **Никогда не хардкодь ключи в коде.**

**Плохо** ❌
```python
API_KEY = "sk-606289..."
```

**Хорошо** ✅
```python
import os
API_KEY = os.getenv("DEEPSEEK_API_KEY")
```

Файл `.env` добавлен в `.gitignore` — не попадёт в git.

---

## Тесты

```bash
python3 -m pytest test_chat.py -v
```

---

## Документация

- [DeepSeek API Docs](https://platform.deepseek.com/api-docs)
