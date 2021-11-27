####################################Task:
# Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
# Тобто, функція приймає два аргументи: список і величину зсуву 
# (якщо ця величина додатня - пересуваємо з кінця на початок,
# якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).

def cyclic_shift(source_list, shift):
    list_length = len(source_list)
    if list_length == 0 or shift == 0:
        print("Data entered incorrectly!")
        return None
    
    from_end = shift > 0
    if not from_end:
        shift = -shift
        
    while shift > 0:
        if from_end:
            source_list.insert(0, source_list.pop())
        else:
            source_list.append(source_list.pop(0))
        shift-=1 
    
    print(source_list)
                  
source_list = [1,2,3,[0,0,0],5]
cyclic_shift(source_list, int(input("Enter the shift value: ")))
