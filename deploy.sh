#!/bin/bash

set -e  # Остановка при ошибке
set -o pipefail

PROJECT_NAME="barblog"
COMPOSE_FILE="compose.yaml"

echo "🚀 Начало развертывания проекта '$PROJECT_NAME'..."

# Проверка Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker не установлен. Установите Docker и повторите попытку."
    exit 1
fi

# Проверка docker compose
if ! docker compose version &> /dev/null; then
    echo "❌ Поддержка 'docker compose' отсутствует. Обновите Docker или используйте 'docker-compose'."
    exit 1
fi

# Создание необходимых директорий
echo "📁 Проверка директорий..."
for dir in media logs staticfiles; do
    if [ ! -d "$dir" ]; then
        echo "✅ Создание директории './$dir'"
        mkdir "$dir"
    fi
done

# Сборка и запуск контейнера
echo "🔧 Сборка контейнеров..."
docker compose -f "$COMPOSE_FILE" build --pull

echo "📦 Запуск контейнеров..."
docker compose -f "$COMPOSE_FILE" up -d

# Проверка состояния
echo "🔍 Состояние контейнеров:"
docker compose -f "$COMPOSE_FILE" ps

echo "✅ Развертывание завершено!"
