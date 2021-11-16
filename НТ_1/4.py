####################################Tasks:
# Write a script to concatenate N strings.

number_of_lines = int(input("Input the number of lines:"))
sentence = []
for line in range(0, number_of_lines):
    sentence.append(input("Input text:"))
print(' '.join(sentence))
