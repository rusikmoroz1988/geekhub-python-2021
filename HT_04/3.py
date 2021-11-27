####################################Task:
# Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(digit):
    is_prime = True
    if (digit< 0 or digit>1000):
        print('Digit out of range!')
        return False
    
    if digit <= 1:
         return False

    for j in range(2, digit):
        if(digit%j == 0):
            is_prime = False
            break
    return is_prime

print("Digit is prime: ", is_prime(int(input('Enter the digit: ')))) 