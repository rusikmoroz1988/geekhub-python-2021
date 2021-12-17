####################################Task:
# Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
# На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
# Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, 
# ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, 
# то що виводити на місці середнього блоку символів?)
# В репозиторій додайте і ті файли, по яким робили тести.
# Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, 
# а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. 
# В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.

class СharacterСountMismatch(Exception):
    def __init__(self, text):
        self.txt = text

def get_symbols_from_file(file_name, number_of_characters):
        
     with open(file_name, "r", encoding="utf-8") as f:
        text_from_file = f.read()
        list_symb = [item for item in text_from_file if item != '\n']
        
        try:
            if number_of_characters==0 or ((number_of_characters * 3) > len(list_symb)):
                raise СharacterСountMismatch("Incorrect number of characters entered")
        except СharacterСountMismatch as myError:
            print(myError)
            return
        
        strt_idx = (len(list_symb) // 2) - (number_of_characters // 2)
        end_idx = (len(list_symb) // 2) + (number_of_characters // 2)
        result = list_symb[strt_idx: end_idx + 1]
        if len(result) > number_of_characters:
            result = list_symb[strt_idx: end_idx]
        
        print(''.join(list_symb[:number_of_characters]), ''.join(result), ''.join(list_symb[-number_of_characters:]))

get_symbols_from_file('test.txt', int(input("Enter the number of characters: ")))