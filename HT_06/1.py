####################################Task:
# Програма-світлофор.
#   Створити програму-емулятор світлофора для авто і пішоходів.
#   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#   Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Green
#      Yellow     Green
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green

import time

def print_colors(colors_avto, colors_ped, step):
    item_avto = colors_avto[step]
    item_ped = colors_ped[step]
    print(item_avto, (15 - len(item_avto) - len(item_ped)) * " ", item_ped)  
    time.sleep(1)
    
def start_traffic_light():
    colors_avto = 4*['Red'] + 2 *['Yellow'] + 4*['Green'] + 2*['Yellow']
    colors_ped = 6*['Green'] + 6 *['Red']
    
    step = 0
    while True: 
        try:
            print_colors(colors_avto, colors_ped, step)
            step+=1
        except KeyboardInterrupt:
            break
        except IndexError:
           step = 0
        
start_traffic_light()