import os
file_path='trash.txt'
with open('file_path', 'w', encoding='utf-8') as file:
    file.write('Привет,мир! \n')
    file.write('Я учусь работать с файлами. \n')
if os.path.exists(file_path):
    print("Файл успешно создан:", file_path)

with open('file_path', 'a', encoding='utf-8') as file:
    file.write("Добавленная строка 1\n")
    file.write("Добавленная строка 2\n")
print("Текст добавлен")

print("\n Содержимое файла:")
with open('file_path', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

os.system(f'notepad "{file_path}"')
    