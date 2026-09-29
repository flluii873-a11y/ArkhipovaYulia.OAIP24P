import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        group_name TEXT NOT NULL,
        grade INTEGER NOT NULL,
        age INTEGER
    )
''')
conn.commit()

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    students_data = [
        ('Иванов Иван', 'ИСП-101', 5, 19),
        ('Петров Пётр', 'ИСП-101', 4, 18),
        ('Сидоров Алексей', 'ИСП-102', 3, 20),
        ('Смирнова Анна', 'ИСП-102', 5, 19),
        ('Кузнецов Максим', 'ИСП-101', 4, 18)
    ]
    cursor.executemany('INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)', students_data)
    conn.commit()

def show_all():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def add_student():
    name = input("ФИО: ")
    group_name = input("Группа: ")
    grade = int(input("Оценка: "))
    age = int(input("Возраст: "))
    cursor.execute('INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)',
                   (name, group_name, grade, age))
    conn.commit()
    print("Студент добавлен.")

def search_by_group():
    group_name = input("Введите группу: ")
    cursor.execute("SELECT * FROM students WHERE group_name = ?", (group_name,))
    for row in cursor.fetchall():
        print(row)

def search_by_grade():
    grade = int(input("Введите оценку: "))
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    for row in cursor.fetchall():
        print(row)

def update_grade():
    student_id = int(input("ID студента: "))
    new_grade = int(input("Новая оценка: "))
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    print("Оценка изменена.")

def delete_student():
    student_id = int(input("ID студента для удаления: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Оставшиеся студенты:")
    show_all()

# Доп. задание: средняя оценка
def average_grade():
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()[0]
    print(f"Средняя оценка: {avg}")


while True:
    print("\n==== УЧЁТ СТУДЕНТОВ ====")
    print("1. Показать всех студентов")
    print("2. Добавить студента")
    print("3. Найти студентов по группе")
    print("4. Найти студентов по оценке")
    print("5. Изменить оценку")
    print("6. Удалить студента")
    print("7. Средняя оценка (доп. задание)")
    print("0. Выход")
    
    choice = input("Выберите пункт: ")
    
    if choice == '1':
        show_all()
    elif choice == '2':
        add_student()
    elif choice == '3':
        search_by_group()
    elif choice == '4':
        search_by_grade()
    elif choice == '5':
        update_grade()
    elif choice == '6':
        delete_student()
    elif choice == '7':
        average_grade()
    elif choice == '0':
        break
    else:
        print("Неверный ввод.")

conn.close()
print("Программа завершена.")