# persons_video_cv
Распознавание лиц в кадре из видео

## Запуск
1. Создать окружение `python -m venv venv`
2. Активировать окружение `source venv/bin/activate`

## Структура
* __data/__ - каталог файлов с видео для обработки
* __logs/__ - логирование проекта
* __notebooks/__ - питоновские ноутбуки для прототипирования
* __src/__ - основной каталог проекта с кодом
* __tests/__ - тесты проекта

## Collaboration
### Code style
* Используйте линтер `flake8`
* Используйте `black` для форматирования кода

### Git flow
* Каждая ветки должна идти от ветки `dev` и соответствовать github issue

### Git commit message style
* Примеры сообщений:
    * `git commit -m "feature: new class for read mp4`
    * `git commit -m "fix: fix incorrect timestamp parsing`
    * `git commit -m "docs: update README`
    * `git commit -m "refactor: formatting black`
* Типы сообщений:
    * `features` - новая функциональность
    * `fix` - исправление багов
    * `docs` - работа с документацией
    * `refactor` - рефакторинг кода, без измения функциональных компонет
