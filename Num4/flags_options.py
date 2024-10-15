import argparse


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

    # Открываем файл для записи
    with open("Num4\output_log.txt", "a") as log_file:
        # Логгирование и вывод в зависимости от флага verbose
        if args.verbose:
            message = f"Verbose Mode: Processing number {args.number} and string '{args.text}'\n"
            print(message, end="")
            log_file.write(message)

        # Повторение строки в зависимости от значения флага repeat
        repeat_count = args.repeat if args.repeat else 1

        # Вывод строки несколько раз
        for _ in range(repeat_count):
            print(args.text)
            log_file.write(f"{args.text}\n")


# Запуск программы
if __name__ == "__main__":
    main()
