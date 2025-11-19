![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![ASUS](https://img.shields.io/badge/asus-000080.svg?style=for-the-badge&logo=asus&logoColor=white)
![Samsung](https://img.shields.io/badge/Samsung-%231428A0.svg?style=for-the-badge&logo=samsung&logoColor=white)

# BarBlog

Информационная система и блог-платформа на базе `Django` и `wagtail`.
Создана в личных целях, для размещения научно-популярных статей, аналитики, 
в том числе о программировании.

## Docker compose

В Windows 11 можно развернуть в `Docker` с помощью `dockerc-start.bat`.

Необходимо через переменные окружения передать информацию по доступу к базе
данных `postgresql`. Перед запуском сделать миграции Django. **Важно**: 
серверная сборка `compose.yaml` предусматривает развёртывание образа
postgresql в докере.

На Linux проще всего использовать стартовый файл "из коробки":
```shell
./deploy.sh
```

Для запуска вручную, можно использовать следующие команды:
```shell
docker compose down
docker compose up -d
docker compose logs -f web
```

При первичной настройке на Linux скорее всего понадобится предоставить право
доступа для user из контейнера к серверным папкам, проброшенным наружу. 
Например, к `logs` или `media`.
```shell
sudo chown -R 1000:1000 ./logs ./media ./staticfilesу
```

## Основные использованные технологии

- Python
- [Django](https://www.djangoproject.com/) 
и [Wagtail](https://docs.wagtail.org/)
- Postgresql
- Docker Compose
- Node и Webpack

## Версии

- _19.11.2025_ — первичное размещение на сервере, устранение "детских"
болезней, дополнено визуальной стилизацией.
- _17.11.2025_ — запуск проекта, первичная сборка. 

## Автор
* [Shindler7](https://github.com/Shindler7)


![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)