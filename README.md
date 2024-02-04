![example workflow](https://github.com/Michelin90/scrapy_parser_pep/actions/workflows/main.yml/badge.svg?style=for-the-badge)
# scrapy_parser_pep
Асинхронный парсер документов PEP на базе фреймворка Scrapy. 
Собирает информацию с ресурса https://peps.python.org/

Парсер выводит собранную информацию в два файла .csv:
1. В первый файл  выводится список всех PEP: номер, название и статус.
2. Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

## Язык и инструменты:
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-blue?style=for-the-badge&logo=scrapy)](https://scrapy.org/)

## Автор:
Михаил [Michelin90](https://github.com/Michelin90) Хохлов

## Подотовка проекта к запуску:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Michelin90/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Запуск парсера:
Для запуска парсера необходимо выполнить команду в корневой директории проекта:
```
scrapy crawl pep
```
Результаты работы парсера будут созданы в директории **results/** 