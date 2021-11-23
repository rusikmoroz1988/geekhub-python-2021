####################################Task:
# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" 
# -> просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# - якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# - якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# - якщо довжина бульше 50 - > ваша фантазiя

def process_range_30_50(list_of_numbers, list_of_non_numbers):
    print("Number of letters: ", len(list_of_non_numbers))
    print("Number of digits: ", len(list_of_numbers))     

def process_range_less_30(list_of_numbers, list_of_non_numbers):
    print("Summ of digits: ", sum([int(item) for item in list_of_numbers])) 
    print("String without digits: ", ' '.join(list_of_non_numbers))   

def process_range_greater_50(list_of_numbers):
    print("Maximum value of digits: ", max(list_of_numbers))
    print("Minimum value of digits: ", min(list_of_numbers))

def process_string(incoming_line):
    list_of_numbers = [symbol for symbol in incoming_line if symbol.isdigit()]
    list_of_non_numbers = [symbol for symbol in incoming_line if not symbol.isdigit()]
    line_length = len(incoming_line)
    if 30 <= line_length <= 50:
        print('Length: ', line_length)
        process_range_30_50(list_of_numbers, list_of_non_numbers)
    elif line_length < 30:
        process_range_less_30(list_of_numbers, list_of_non_numbers) 
    else:
        process_range_greater_50(list_of_numbers)

process_string(input("Enter a string of characters: "))