# Frontend - TonAvto Offer

React приложение для управления предложениями и покупками.

## Быстрый старт

```bash
# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev

# Сборка для продакшена
npm run build

# Просмотр продакшен сборки
npm run preview
```

## Структура

- `src/api/client.js` - API клиент для работы с бекендом
- `src/components/` - React компоненты
  - `OfferList.jsx` - Список и управление предложениями
  - `OfferForm.jsx` - Форма создания/редактирования предложений
  - `BuyList.jsx` - Список и управление покупками
  - `BuyForm.jsx` - Форма создания/редактирования покупок
- `src/App.jsx` - Главный компонент приложения
- `src/App.css` - Стили приложения

## Настройка API

API URL настраивается в `src/api/client.js`. По умолчанию используется `http://localhost:8000/api`.
