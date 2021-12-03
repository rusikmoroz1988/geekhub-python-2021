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

def print_colors(colors_avto, colors_ped, step = 0):
    try:
        item_avto = colors_avto[step]
        item_ped = colors_ped[step]
        print(item_avto, (15 - len(item_avto) - len(item_ped)) * " ", item_ped)
        step+=1
    except:
        step=0          
    time.sleep(1)
    print_colors(colors_avto, colors_ped, step)
    

def start_traffic_light():
    colors_avto = 4*['Red'] + 2 *['Yellow'] + 4*['Green'] + 2*['Yellow']
    colors_ped = 6*['Green'] + 6 *['Red']
    print_colors(colors_avto, colors_ped)

start_traffic_light()