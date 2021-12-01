####################################Task:
# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) 
# і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, 
# якщо було повернено останній елемент із послідовності - ітерація починається знову.
#   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#   >>>for elem in generator([1, 2, 3]):
#   ...    print(elem)
#   ...
#    1
#    2
#    3
#    1
#    2
#    3
#    1
#    .......

def generator(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    step = 1    
    while saved:
        for element in saved:
              yield element
              if step==len(saved):
                  gen_iterator = generator(iterable)
                  next(gen_iterator)
              step+=1  
                
for elem in generator([1,2,3]):
    print(elem)