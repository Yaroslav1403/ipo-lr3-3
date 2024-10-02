day = int(input("Введите день (число): "))
month = int(input("Введите месяц (число): "))
if (month == 3 and day >= 1) or (month in [4, 5]) or (month == 6 and day < 1):
    season = "Весна"
elif (month == 6 and day >= 1) or (month in [7, 8]) or (month == 9 and day < 1):
    season = "Лето"
elif (month == 9 and day >= 1) or (month in [10, 11]) or (month == 12 and day < 1):
    season = "Осень"
else:
    season = "Зима"
print(f"Дата: {day}/{month} - это {season}")
