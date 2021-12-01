####################################Task:
# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: 
# https://docs.python.org/3/library/stdtypes.html#range

def my_range(start=0, stop=None, step=1):
    if stop==None and start!=0:
        stop = start     
        start = 0
        
    if step == 0:
        raise ValueError("argument 'step' should not be zero!")
    
    if stop == 0:
        raise ValueError("argument 'stop' should not be zero!")

    if start<stop and step<0:
        raise TypeError("argument 'step' should not be {}".format(step))

    if start < stop:
        while start < stop:    
            yield start
            start+=step
    else:
        while start>stop and step<0:
            yield start
            start+=step           
    return start

print(list(my_range(1,10,2)))
print(list(range(1,10,2)))

print(list(my_range(8)))
print(list(range(8)))