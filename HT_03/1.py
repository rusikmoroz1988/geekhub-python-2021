####################################Task:
# Створити цикл від 0 до ... (вводиться користувачем). 
# В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

input_number = int(input("Please enter a number: "))
result = [item for item in range(input_number + 1) if item % 17 == 0]
for step in result:
    print(step)
