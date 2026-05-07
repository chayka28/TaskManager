# TaskManager

---

## Установка:

    python -m venv .venv

## Windows:

    .venv\Scripts\activate

## Linux/macOS:

    source .venv/bin/activate

## установка зависимостей

    pip install -r requirements.txt

## запуск

    uvicorn main:app --reload

---

## Эндпоинты

**POST /tasks** — создание задачи. Обязательные поля: title (str), status (new/in_progress/done). Опционально: description (str). Регистр status не учитывается. Возвращает 201 Created и объект с id.

**GET /tasks** — список всех задач. Возвращает 200 OK и массив объектов.

**GET /tasks/{task_id}** — получение задачи по ID. Возвращает 200 OK или 404 Not Found, если задача не найдена.

---

## Структура проекта

main.py — контроллер (маршруты FastAPI)
schemas.py — Pydantic-модели для валидации запросов и описания ответов
services.py — операции с задачами и хранение в памяти
requirements.txt — список зависимостей

---

## Примечание

Данные хранятся в оперативной памяти и полностью сбрасываются при перезапуске сервера.
