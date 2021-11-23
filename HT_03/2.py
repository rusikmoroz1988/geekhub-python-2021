####################################Task:
# Користувачем вводиться початковий і кінцевий рік. 
# Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно)

start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: ")) + 1
result = [item for item in range(start_year, end_year) if (item % 400 == 0 or (item % 100 != 0 and item % 4 == 0))]
for year in result:
    print(year)