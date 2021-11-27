####################################Task:
# Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, 
# що не перевищують його.

def fibonacci(argument):
    if argument <= 0:
        print('Data entered incorrectly!')
        return None

    sequence = [0, 1]
    while True:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        if next_value > argument:
            break
        sequence.append(next_value)

    [print(item) for item in sequence]

argument = int(input("Please enter the argument: "))
fibonacci(argument)

