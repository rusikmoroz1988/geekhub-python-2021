####################################Task:
# Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > 
# одиниць строком на < years > років під < percents > відсотків 
# (кожен рік сума вкладу збільшується на цей відсоток, 
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). 
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). 
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank(a, years, percents = 10):
    for year in range(years, 0, -1):
        a += a*percents/100  
    return a       

deposit_amount = eval(input("Enter the size of the deposit: "))
number_of_years = int(input("Enter number of years: "))
print('Sum:', bank(deposit_amount, number_of_years))