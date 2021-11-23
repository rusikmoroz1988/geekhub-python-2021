####################################Task:
# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), 
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(number_month):
    result = ''
    seasons = dict()
    seasons[(12,1,2)] = "Winter"
    seasons[(3,4,5)] = "Spring"
    seasons[(6,7,8)] = "Summer"
    seasons[(9,10,11)] = "Autumn"
    for key,value in seasons.items():
        if not number_month in key:
            continue
        result = value
        break
    if not len(result):
        print('There is no such season!')
    else:
        print(result)

season(int(input('Enter the month number: ')))