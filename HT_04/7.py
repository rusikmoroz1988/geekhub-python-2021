####################################Task:
# Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

from collections import Counter

def same_elements(*args):
    incoming_list = list(args)
    result = {k:v for k,v in Counter(incoming_list).items()}
    print('\n'.join(str(key) +" - "+str(value) for key, value in result.items()))

same_elements(1, 3, 3, 1, 1, 1, 1, 'g')