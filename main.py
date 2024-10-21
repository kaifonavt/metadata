import os
from PIL import Image
from exif import Image as ExifImage

# Функция для изменения только даты в метаданных EXIF
def change_metadata(image_path, new_date):
    try:
        # Открываем изображение
        with open(image_path, 'rb') as img_file:
            img = ExifImage(img_file)

        # Проверяем, есть ли метаданные
        if img.has_exif:
            original_datetime = img.datetime_original
            print(f"Оригинальная дата и время: {original_datetime}")

            # Разделяем дату и время
            original_time = original_datetime.split(' ')[1]  # Оставляем время

            # Меняем только дату, оставляя время неизменным
            img.datetime_original = f"{new_date} {original_time}"
            
            # Сохраняем изменения
            with open(image_path, 'wb') as new_img_file:
                new_img_file.write(img.get_file())
            
            print(f"Новая дата для {image_path}: {new_date} {original_time}")
        else:
            print(f"Изображение {image_path} не содержит метаданных EXIF.")
    
    except Exception as e:
        print(f"Ошибка при обработке {image_path}: {e}")

# Функция для работы с каталогом
def process_images_in_directory(directory_path, new_date):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, filename)
            change_metadata(image_path, new_date)

# Основная часть программы
if __name__ == "__main__":
    # Вводим путь до каталога
    directory = input("Введите путь к каталогу с изображениями: ")
    
    # Вводим новую дату (без времени)
    new_metadata_date = input("Введите новую дату (например, '2024:10:19'): ")
    
    # Обрабатываем изображения в каталоге
    process_images_in_directory(directory, new_metadata_date)
