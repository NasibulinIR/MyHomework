class Task():
    def __init__(self, name, due_date, mark_status):
        self.name = name
        self.due_date = due_date
        self.mark_status = mark_status

def load_tasks():
    task_list = []
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                parts = line.split(',')
                if len(parts) == 3:
                    name, due_date, mark_status = line.strip().split(',')
                    task = Task(name, due_date, mark_status)
                    task_list.append(task)
                else:
                    print(f"Некорректная строка в файле: {line.strip()}")
        return task_list
    except FileNotFoundError:
        print("Файл tasks.txt не был найден. Создан новый список задач.")
        return []

def save_task(task_list):
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for task in task_list:
            file.write(f"{task.name},{task.due_date},{task.mark_status}\n")


def add_task(task_list):
    name = input("Введите название задачи: ")
    due_date = input("Введите дату выполнения задачи (дд.мм.гг): ")
    mark_status = 'X'
    task = Task(name, due_date, mark_status)
    task_list.append(task)
    save_task(task_list)
    print("Задача успешно добавлена.")

def check_tasks(task_list):
    for task in task_list:
        print(f"{task.name} - {task.due_date} - {task.mark_status}")

def mark_task_as_done(task_list):
    task_name = input("Введите название задачи, которую хотите отметить как выполненную: ")
    for task in task_list:
        if task.name == task_name:
            task.mark_status = 'V'
            save_task(task_list)
            print("Задача успешно отмечена как выполненная.")
            return
    print("Задача с таким названием не найдена.")

def list_of_undone_tasks(task_list):
    inner_undone_tasks = []
    for task in task_list:
        if task.mark_status == 'X':
            inner_undone_tasks.append(task)
    return inner_undone_tasks

tasks = load_tasks()

while True:
    print("\nВыберите действие:")
    print("1. Добавить задачу")
    print("2. Проверить задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Проверить невыполненные задачи")
    print("5. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        print("Список задач:")
        check_tasks(tasks)
    elif choice == '3':
        mark_task_as_done(tasks)
    elif choice == '4':
        undone_tasks = list_of_undone_tasks(tasks)
        print("Список невыполненных задач:")
        check_tasks(undone_tasks)
    elif choice == '5':
        save_task(tasks)
        print("Работа программы завершена")
        break
    else:
        print("Некорректный ввод. Пожалуйста, попробуйте еще раз.")

