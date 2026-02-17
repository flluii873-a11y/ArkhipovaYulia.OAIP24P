import json
import os

data_file="data.json"

def load_data():
    if not os.path.exists(data_file):
        return []  
    
    try:
        with open(data_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return [] 

def save_data(data):
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
def get_next_project_id(data):
    if not data:
        return 1
    return max(project['id'] for project in data) + 1

def show_projects(data): #показ проектов
    print("\nСписок проектов")
    if not data:
        print("Проектов пока нет")
        return

    for project in data: #кол-во задач
        task_count=len(project.get('tasks', []))
        print(f"ID: {project['id']}  Название: {project['name']} Статус: {project['status']} Задач: {task_count}")

def create_project(data): #новые проекты
    name=input("Введите название проекта: ").strip()
    if not name:
        print("Введи название пж")
        return

    new_project={
        "id": get_next_project_id(data),
        "name": name,
        "status": "",
        "tasks": [] #пустой список задач
    }
    
    data.append(new_project)
    save_data(data)
    print(f"Проект '{name}' успешно создан!")

def add_task(data): #добавить задачу
    show_projects(data)
    if not data: return

    try:
        project_id=int(input("Введи ID проекта, куда добавить задачу: "))
    except ValueError:
        print("Нужно числоо")
        return

    #проект с таким ID
    project=next((p for p in data if p['id']==project_id), None)

    if not project:
        print("Проект с таким ID нету")
        return

    task_name=input("Введите название задачи: ").strip()
    if not task_name:
        print("Введи задачууу")
        return

    #создаем задачу
    new_task={
        "name": task_name
    }
    
    project['tasks'].append(new_task)
    save_data(data)
    print(f"Задача '{task_name}' добавлена в проект '{project['name']}'")

def show_tasks(data): #показать все задачи
    show_projects(data)
    if not data: return

    try:
        project_id=int(input("Введи ID проекта,чтобы увидеть задачи: "))
    except ValueError:
        print("Нужно числоо")
        return

    project=next((p for p in data if p['id']==project_id), None)

    if not project:
        print("Проекта нету")
        return

    print(f"\nЗадачи проекта'{project['name']}'")
    if not project['tasks']:
        print("Задач нету")
    else:
        for i, task in enumerate(project['tasks'], 1):
            print(f"{i}. {task['name']}")

def change_project_status(data): #меняем статус
    show_projects(data)
    if not data: return

    try:
        project_id=int(input("Введи ID проекта для изменения статуса: "))
    except ValueError:
        print("Надо числоо")
        return

    project=next((p for p in data if p['id'] == project_id), None)

    if not project:
        print("Проект не найден")
        return

    print("\nДоступные статусы:")
    print("1. Планирование")
    print("2. В работе")
    print("3. Готов")
    
    choice=input("Выберите номер статуса (1-3): ")
    
    status_map={
        "1": "Планирование",
        "2": "В работе",
        "3": "Готов"
    }

    if choice in status_map:
        project['status']=status_map[choice]
        save_data(data)
        print(f"Статус проекта '{project['name']}' изменен на '{project['status']}'")
    else:
        print("Неверный выбор")

def main():
    print("Привет, ты в своих проектах")
    
    while True:
        print("\n Меню")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Добавить задачу")
        print("4. Показать задачи проекта")
        print("5. Изменить статус проекта")
        print("0. Выход")

        choice=input("Выбери действие: ")
        data=load_data()

        if choice=='1':
            show_projects(data)
        elif choice=='2':
            create_project(data)
        elif choice=='3':
            add_task(data)
        elif choice=='4':
            show_tasks(data)
        elif choice=='5':
            change_project_status(data)
        elif choice=='0':
            print("Поки")
            break
        else:
            print("Не то вводишь")

if __name__ == "__main__":
    main()