####################################Tasks:
# Write a script to print out a set containing all the colours from color_list_1 
# which are not present in color_list_2

color_list_1 = input("Input first color list:").split(",")
color_list_2 = input("Input second color list:").split(",")
result = set(color_list_1) - set(color_list_2)
print(result)