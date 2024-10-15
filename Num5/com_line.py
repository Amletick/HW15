import os
import logging
from collections import namedtuple
import argparse

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def setup_logging(log_file_path):
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )


def gather_directory_info(directory_path):
    # Проверяем, что переданный путь - это директория
    if not os.path.isdir(directory_path):
        raise ValueError(f"'{directory_path}' не является директорией или не существует.")

    directory_content = []

    # Проход по содержимому директории
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        parent_directory = os.path.basename(os.path.abspath(directory_path))

        # Если это файл, разделяем на имя и расширение
        if not is_directory:
            name, extension = os.path.splitext(item)
            extension = extension.lstrip('.')
        else:
            name = item
            extension = ''  # Папки не имеют расширений

        # Создаем объект FileInfo и добавляем его в список
        file_info = FileInfo(
            name=name,
            extension=extension,
            is_directory=is_directory,
            parent_directory=parent_directory
        )
        directory_content.append(file_info)

        # Логируем информацию о каждом элементе
        logging.info(f"Объект: {file_info}")

    return directory_content


def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Скрипт для сбора информации о содержимом директории")
    parser.add_argument("directory", type=str, help="Путь до директории для сбора информации")
    args = parser.parse_args()

    # Определение пути для лог-файла
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, "directory_info.log")

    # Настройка логирования
    setup_logging(log_file_path)

    try:
        # Сбор информации о директории
        directory_content = gather_directory_info(args.directory)

        # Выводим информацию для каждого элемента
        for item in directory_content:
            print(
                f"Name: {item.name}, Extension: {item.extension}, Is Directory: {item.is_directory},"
                f" Parent Directory: {item.parent_directory}")

    except ValueError as e:
        logging.error(f"Ошибка: {e}")
        print(f"Ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
