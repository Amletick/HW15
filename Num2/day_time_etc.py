from datetime import datetime

# Получаем текущее время и дату
current_datetime = datetime.now()

# Форматируем дату и время в строку
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Получаем название дня недели
day_of_week = current_datetime.strftime('%A')

# Получаем номер недели в году
week_number = current_datetime.isocalendar()[1]

# Формируем строку для записи в файл
output = (f"Текущая дата и время: {formatted_datetime}\n"
          f"День недели: {day_of_week}\n"
          f"Номер недели в году: {week_number}\n")

# Выводим результат в консоль
print(output)

# Дополнительно в файл:
with open('current_datetime_info.txt', "a") as file:
    file.write(output)
