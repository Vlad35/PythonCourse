import csv

students = []
total_time = 0
count = 0

with open('Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовок

    # Читаем строки файла и пропускаем последние две строки
    rows = list(reader)
    rows = rows[:-2]

    for row in rows:
        name = row[1] + ' ' + row[0]  # Фамилия и Имя
        score = row[9].replace(',', '.')  # Оценка
        time_str = row[8]  # Затраченное время

        if score == '-':
            continue

        if time_str == '-':
            continue

        if float(score) > 7:
            students.append((name, time_str))
            # Разбираем строку с временем
            time_parts = time_str.split()
            if len(time_parts) == 4:
                minutes = int(time_parts[0])
                seconds = int(time_parts[2])
                total_time += minutes * 60 + seconds
                count += 1

students.sort(key=lambda x: x[0])  # Сортируем по ФИО

# Выводим студентов
for student in students:
    print(student[0])

# Вычисляем среднее время
if count > 0:
    average_time = total_time / count
    hours = int(average_time // 3600)
    minutes = int((average_time % 3600) // 60)
    seconds = int((average_time % 3600) % 60)
    print("Среднее время прохождения теста: {} час {} минут {} секунд".format(hours, minutes, seconds))
else:
    print("Нет студентов с оценкой выше 7")
