# TonAvto Offer Management System

Система управления предложениями и покупками с современным веб-интерфейсом.

## Структура проекта

```
TonAvto_Offer/
├── backend/          # FastAPI бекенд
│   ├── src/
│   │   ├── models/   # SQLAlchemy модели
│   │   ├── routes/   # API роуты
│   │   ├── services/ # Бизнес-логика
│   │   ├── repositories/ # Работа с БД
│   │   └── schemas/  # Pydantic схемы
│   └── requieriments.txt
└── frontend/         # React + Vite фронтенд
    ├── src/
    │   ├── components/ # React компоненты
    │   └── api/        # API клиент
    └── package.json
```

## Требования

- Python 3.8+
- Node.js 16+ и npm/yarn
- SQLite (встроен в Python)

## Установка и запуск

### 1. Настройка бекенда

```bash
# Перейдите в директорию бекенда
cd backend

# Создайте виртуальное окружение (рекомендуется)
python -m venv venv

# Активируйте виртуальное окружение
# На Windows:
venv\Scripts\activate
# На macOS/Linux:
source venv/bin/activate

# Установите зависимости
pip install -r requieriments.txt

# Запустите сервер
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Бекенд будет доступен по адресу: `http://localhost:8000`
- API документация: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

### 2. Настройка фронтенда

Откройте новый терминал:

```bash
# Перейдите в директорию фронтенда
cd frontend

# Установите зависимости
npm install

# Запустите dev сервер
npm run dev
```

Фронтенд будет доступен по адресу: `http://localhost:5173`

## Использование

### API Endpoints

#### Offers (Предложения)
- `GET /api/offer` - Получить все предложения
- `POST /api/offer` - Создать предложение
- `PUT /api/offer/{id}` - Обновить предложение
- `DELETE /api/offer/{id}` - Удалить предложение

#### Buys (Покупки)
- `GET /api/buy` - Получить все покупки
- `POST /api/buy` - Создать покупку
- `PUT /api/buy/{id}` - Обновить покупку
- `DELETE /api/buy/{id}` - Удалить покупку

### Веб-интерфейс

1. Откройте `http://localhost:5173` в браузере
2. Переключайтесь между вкладками "Предложения" и "Покупки"
3. Используйте кнопки для создания, редактирования и удаления записей

## Особенности

- ✅ Полный CRUD для Offers и Buys
- ✅ Современный React интерфейс
- ✅ Адаптивный дизайн
- ✅ Валидация форм
- ✅ Обработка ошибок
- ✅ Автоматическое обновление данных

## Решение проблем

### CORS ошибки
Убедитесь, что бекенд запущен и CORS настроен правильно в `backend/src/config.py`

### Порт занят
- Бекенд: измените порт в `backend/src/run.py` или используйте флаг `--port`
- Фронтенд: измените порт в `frontend/vite.config.js`

### База данных
База данных SQLite создается автоматически при первом запуске в `backend/TonAvto.db`

## Разработка

### Бекенд
- Структура: Repository -> Service -> Route
- Используется SQLAlchemy для работы с БД
- Pydantic для валидации данных

### Фронтенд
- React 18 с хуками
- Axios для HTTP запросов
- Vite для быстрой разработки
- CSS модули для стилизации

## Лицензия

MIT
