Клас Task

Клас Task представляє окреме завдання з різними атрибутами, такими як назва, опис, дата завершення, статус, пріоритет, примітки, тривалість, регулярність і залежності.
Методи:

    is_due_today():
        Перевіряє, чи завдання має бути виконане сьогодні.

task.is_due_today()

update_task(**kwargs):

    Оновлює атрибути завдання.


task.update_task(description="Оновлений опис", due_date=date(2024, 5, 26))

add_dependency(task) / remove_dependency(task):

    Додає або видаляє залежності між завданнями.


    task1.add_dependency(task2)
    task1.remove_dependency(task2)

Клас Schedule

Клас Schedule керує кількома завданнями і надає різні методи для взаємодії з ними.
Методи:

    add_task(task) / remove_task(task_title) / get_task(task_title):
        Додає, видаляє та отримує завдання з розкладу.


schedule.add_task(task)
schedule.remove_task("Купити продукти")
schedule.get_task("Купити продукти")

list_overdue_tasks() / list_tasks_due_today():

    Показує завдання, які прострочені або мають бути виконані сьогодні.


schedule.list_overdue_tasks()
schedule.list_tasks_due_today()

sort_tasks_by_due_date():

    Сортує завдання за датою завершення.


schedule.sort_tasks_by_due_date()

update_task(task_title, **kwargs):

    Оновлює атрибути конкретного завдання.


schedule.update_task("Купити продукти", status="Завершено")

list_tasks_by_priority(priority):

    Показує завдання з певним пріоритетом.


schedule.list_tasks_by_priority("Високий")

save_to_file(filename) / load_from_file(filename):

    Зберігає та завантажує завдання у/з файл(у).

schedule.save_to_file("розклад.txt")
schedule.load_from_file("розклад.txt")

list_all_tasks() / list_completed_tasks():

    Показує всі завдання або завершені завдання.

schedule.list_all_tasks()
schedule.list_completed_tasks()

find_task_by_keyword(keyword):

    Знаходить завдання за ключовим словом у назві або описі.


schedule.find_task_by_keyword("завдання")

check_deadlines():

    Показує завдання, які мають бути виконані в найближчі 24 години.


schedule.check_deadlines()

weekly_schedule(start_date) / monthly_schedule(year, month):

    Показує завдання на тиждень, що починається з вказаної дати, або на певний місяць.


schedule.weekly_schedule(date(2024, 5, 20))
schedule.monthly_schedule(2024, 5)

list_tasks_by_duration(min_duration, max_duration):

    Показує завдання, час виконання яких потрапляє в зазначений діапазон.


schedule.list_tasks_by_duration(1, 3)

task_history():

    Повертає історію додавання, видалення або оновлення завдань.


schedule.task_history()

clear_completed_tasks():

    Видаляє всі завершені завдання з розкладу.


schedule.clear_completed_tasks()

list_tasks_with_notes() / list_recurring_tasks():

    Показує завдання з примітками або регулярні завдання.


schedule.list_tasks_with_notes()
schedule.list_recurring_tasks()

set_reminder(task_title, reminder_date):

    Встановлює нагадування для певного завдання.

schedule.set_reminder("Купити продукти", date(2024, 5, 24))

completion_percentage():

    Розраховує відсоток завершених завдань.

schedule.completion_percentage()