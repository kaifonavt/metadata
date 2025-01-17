# Batch Image Metadata Modifier

Этот скрипт на Python позволяет пакетно изменять **EXIF метаданные** (в частности, дату) изображений в заданном каталоге. Он сохраняет оригинальное время и обновляет только дату на ту, что введёт пользователь.

## Особенности

- **Пакетная обработка**: Скрипт обрабатывает все изображения в указанном каталоге.
- **Изменение EXIF даты**: Обновляется только дата, при этом оригинальное время остаётся неизменным.
- **Поддерживаемые форматы**: Работает с изображениями форматов `.jpg`, `.jpeg`, и `.png`.

## Требования

Перед запуском скрипта необходимо установить следующие библиотеки Python:

- `Pillow` для работы с изображениями
- `exif` для работы с EXIF метаданными

Вы можете установить их с помощью `pip`:

```bash
pip install pillow exif
