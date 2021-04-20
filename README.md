# persons_video_cv
Распознавание лиц в кадре из видео

## Запуск проекта
### Инициализация проекта
1. Создать окружение `python -m venv venv`
2. Активировать окружение `source venv/bin/activate`
3. Установить зависимости проекта: `pip install -r requirements.txt`

### Преобразование видео файла в тензор
Данные скрипт читает видео файл. Файл должен находится на диске, в директории data.
На выходе получается тензор для дальнейшей работы
```python
from src.reader import VideoFileReader
video_file = VideoFileReader('./data/your_file.mp4')

# Получить количество кадров в файле
video_file.frame_count
>>> 1713

# Получение тензора из файла
frame_list = video_file.get_frames

frame_list[0]  # Первый кадр из видео
frame_list[:5]  # Первые 5 кадров
```

### Получение видео из ютуб
На вход подается url видео трансляции с ютуба, на выходе просмотр видео, и вывод тензора в консоль.
```python
from src.reader import YouTubeReader
video_file = YouTubeReader('https://www.youtube.com/watch?v=UZ_-6NDQAxM&t=605s')

# Запуск воспроизведения и вывод тензора в консоль
video_file.show_video()
```


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
  