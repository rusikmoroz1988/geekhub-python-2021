####################################Task:
# Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, 
# і вертатиме список простих чисел всередині цього діапазона.

def prime_list(start, finish):
    prime_list = []
    for i in range(start, finish):
        if i > 1:
            for j in range(2,i):
                if(i % j == 0):
                    break
            else:
                prime_list.append(i)
    return prime_list

start = int(input("Please enter the start number: "))
finish = int(input("Please enter the finish number: "))
[print(item) for item in prime_list(start, finish)]