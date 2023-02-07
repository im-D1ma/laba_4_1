import sys
with open ('aristotle.txt') as file:
    file_full=file.read()
count_all = len (file_full)
print ('Общее количество символов: ', count_all)

with open ('aristotle.txt') as file:
    file_clean=file.read().replace(' ', '').replace('\r', '').replace('\n', '')
count_no_space = len (file_clean)
print ('Количество символов без пробелов: ', count_no_space)

with open ('aristotle.txt') as file:
    file_no_point=file.read()
    count_no_point = file_no_point.count('.')
    count_no_point += file_no_point.count(',')
    count_no_point += file_no_point.count('!')
    count_no_point += file_no_point.count('?')
    count_no_point += file_no_point.count('-')
    count_no_point += file_no_point.count(':')
    count_no_point += file_no_point.count('_')
    count_no_point += file_no_point.count('"')
    count_no_point += file_no_point.count("'")
    count_no_point += file_no_point.count("...")

print ('Количество символов без знаков препинания: ', count_no_point)

with open ('aristotle.txt') as file:
    file_word=file.read().split()
count_word = len (file_word)
print ('Количество сслов: ', count_word)
