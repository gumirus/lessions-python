'''
Работа с файлами.

Цель: Целью данной работы является наработка навыков работы 
с файлами с помощью языка программирования Python.

Что нужно сделать: 

1 - Создайте текстовый файл с названием "sample.txt" и написать 
программу для чтения и вывода его содержимого на экран.

'''

# Создание файла ("w" - запись)
with open('sample.txt', 'w') as file:
    file.write("Домашнее задание #5 - выполнено!")

# Чтение файла ("r"- чтение) и вывод содержимого на экран
with open('sample.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
