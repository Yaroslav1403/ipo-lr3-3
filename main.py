#Просим пользователя ввести день, и, преобразовав в целое число, программа сохраняет это значение в переменную day
day = int(input("Введите день (число): "))
#Просим пользователя ввести месяц, и, преобразовывав в целое число, программа сохраняет это значение в переменную month
month = int(input("Введите месяц (число): "))
#Проверим, является ли введенный день меньше 1 или месяц меньше 1 или больше 12
if day < 1 or month < 1 or month > 12:
        #Если хотя бы одно из условий истинно, то программа выводит: "Введена неккоректная дата."
        print("Введена неккоректная дата.")
else:
    #Создаём список для определения количества дней в каждом месяце года
    days_in_all_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Проверяем, не превышает ли введенный день количество дней в соответствующем месяце
if day > days_in_all_months [month - 1]:
        #Если введённый день превышает количество дней в соответствующем месяце, то программа выводит: "Введена неккоректная дата."
        print("Введена неккоректная дата.")
else:
#Проверяем, к какому времени года относится дата, введённая пользователем   
    if (month == 3 and day >= 1) or (month in [4, 5]) or (month == 6 and day < 1):
        season = "весна"
    elif (month == 6 and day >= 1) or (month in [7, 8]) or (month == 9 and day < 1):
        season = "лето"
    elif (month == 9 and day >= 1) or (month in [10, 11]) or (month == 12 and day < 1):
        season = "осень"
    elif (month == 12 and day >= 1) or (month in [1, 2]) or (month == 2 and day < 1):
        season = "зима"
#Выводим результат
print(f"Дата: {day}/{month} - это {season}")
