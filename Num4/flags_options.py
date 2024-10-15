import argparse
import os


def main():
    # Создание парсера для аргументов командной строки
    parser = argparse.ArgumentParser(
        description="Script to process a number and a string with options for verbosity and repetition.")

    # Обязательные аргументы
    parser.add_argument("number", type=int, help="Input number")
    parser.add_argument("text", type=str, help="Input text string")

    # Опции
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--repeat", type=int, help="Number of times to repeat the string")

    # Парсинг аргументов
    args = parser.parse_args()

    # Получаем путь к папке со скриптом
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, "output_log.txt")

    # Открываем файл для записи
    with open(log_file_path, "a") as log_file:
        # Запись аргументов командной строки в файл
        command_message = f"Command executed: number={args.number}, text='{args.text}', verbose={args.verbose}, repeat={args.repeat}\n"
        print(command_message)
        log_file.write(command_message)

        # Логгирование и вывод в зависимости от флага verbose
        if args.verbose:
            verbose_message = f"Verbose Mode: Processing number {args.number} and string '{args.text}'\n"
            print(verbose_message, end="")
            log_file.write(verbose_message)

        # Повторение строки в зависимости от значения флага repeat
        repeat_count = args.repeat if args.repeat else 1

        # Вывод строки несколько раз
        for _ in range(repeat_count):
            print(args.text)
            log_file.write(f"{args.text}\n")


# Запуск программы
if __name__ == "__main__":
    main()
