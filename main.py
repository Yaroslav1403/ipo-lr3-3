# Пользователь должен ввести значения дня и месяца
day = int(input("Введите день (число): "))
month = int(input("Введите месяц (число): "))
# Проверим на отрицательный день или месяц
if day < 1 or month < 1 or month > 12:
        print("Введена неккоректная дата.")
else:
# Определяем количество дней в каждом месяце года
    days_in_all_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day > days_in_all_months [month - 1]:
        print("Введена неккоректная дата.")
else:
# Проверяем, к какому времени года относится дата, введённая пользователем   
    if (month == 3 and day >= 1) or (month in [4, 5]) or (month == 6 and day < 1):
        season = "Весна"
    elif (month == 6 and day >= 1) or (month in [7, 8]) or (month == 9 and day < 1):
        season = "Лето"
    elif (month == 9 and day >= 1) or (month in [10, 11]) or (month == 12 and day < 1):
        season = "Осень"
    elif (month == 12 and day >= 1) or (month in [1, 2]) or (month == 2 and day < 1):
        season = "Зима"
#Вывод результата
print(f"Дата: {day}/{month} - это {season}")
