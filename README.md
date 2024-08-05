# Проект асинхронного парсинга информации о PEP
Данный проект представляет собой парсер, построенный на базе фреймворка Scrapy и позволяющий собирать основную информацию о всех документах PEP для последующего сохранения в файл. Дополнительно парсер собирает информацию о актуальных статусах всех документов PEP и производит их подсчет. 
Вся собранная информация сохраняется в файлах формата CSV.

## Стэк используемых технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-60A839?style=for-the-badge&logo=scrapy&logoColor=white)](https://scrapy.org/)

## Разворачивание проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RedCloverfield/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Обновить пакетный менеджер pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск парсера и доступ к справочной информации:
Запуск парсера осуществляется следующей командой

```
scrapy crawl pep
```

Файлы с информацией, собранной парсером сохраняются в папке `results`, которая создается в корневой директории проекта при первом запуске парсера.

Доступ к справочной информации о работе парсера осуществляется с помощью команды

```
scrapy crawl --help
```

## Автор проекта
[Ефимов Станислав](https://github.com/RedCloverfield)