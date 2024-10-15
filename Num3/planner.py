from datetime import datetime, timedelta


def get_future_date(days_from_now):
    # Получаем текущую дату
    current_date = datetime.now()

    # Форматируем текущую дату для записи
    current_date_str = current_date.strftime('%Y-%m-%d')

    # Создаем объект timedelta с количеством дней
    future_date = current_date + timedelta(days=days_from_now)

    # Форматируем будущую дату в строку формата YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')

    # Записываем результат в файл
    with open("future_date_log.txt", "a") as file:
        file.write(f"Запрос от {current_date_str}:\n")
        file.write(f"Дата через {days_from_now} дней: {formatted_future_date}\n\n")

    return formatted_future_date


# Пример использования
days = 30  # Задаем количество дней
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")
