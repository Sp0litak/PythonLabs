from datetime import date

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=0, recurrence=None, dependencies=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies if dependencies else []

    def is_due_today(self):
        return self.due_date == date.today()

    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date}, Status: {self.status}, Priority: {self.priority}"

    def update_task(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'Task' object has no attribute '{key}'")

    def add_dependency(self, task):
        if task not in self.dependencies:
            self.dependencies.append(task)

    def remove_dependency(self, task):
        if task in self.dependencies:
            self.dependencies.remove(task)
class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            self.history.append(("added", task))
        else:
            raise TypeError("Expected an instance of Task class")

    def remove_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                self.history.append(("removed", task))
                return
        raise ValueError(f"Task '{task_title}' not found in the schedule")

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        raise ValueError(f"Task '{task_title}' not found in the schedule")

    def list_overdue_tasks(self):
        today = date.today()
        overdue_tasks = [task for task in self.tasks if task.due_date < today and task.status != "Completed"]
        return overdue_tasks

    def list_tasks_due_today(self):
        today = date.today()
        due_today_tasks = [task for task in self.tasks if task.due_date == today]
        return due_today_tasks

    def sort_tasks_by_due_date(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x.due_date)
        return sorted_tasks

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        task.update_task(**kwargs)
        self.history.append(("updated", task))

    def list_tasks_by_priority(self, priority):
        tasks_by_priority = [task for task in self.tasks if task.priority == priority]
        return tasks_by_priority

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority}\n")

    def load_from_file(self, filename):
        self.tasks = []
        with open(filename, 'r') as file:
            for line in file:
                title, description, due_date_str, status, priority = line.strip().split(',')
                due_date = date.fromisoformat(due_date_str)
                task = Task(title, description, due_date, status=status, priority=priority)
                self.tasks.append(task)

    def list_all_tasks(self):
        return self.tasks

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        task.status = "Completed"
        self.history.append(("updated", task))

    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.status == "Completed"]
        return completed_tasks

    def find_task_by_keyword(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        return matching_tasks

    def check_deadlines(self):
        today = date.today()
        next_day = today + timedelta(days=1)
        upcoming_tasks = [task for task in self.tasks if task.due_date == next_day]
        return upcoming_tasks

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=6)
        weekly_tasks = [task for task in self.tasks if start_date <= task.due_date <= end_date]
        return weekly_tasks

    def monthly_schedule(self, year, month):
        monthly_tasks = [task for task in self.tasks if task.due_date.year == year and task.due_date.month == month]
        return monthly_tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        filtered_tasks = [task for task in self.tasks if min_duration <= task.duration <= max_duration]
        return filtered_tasks

    def task_history(self):
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_tasks_with_notes(self):
        tasks_with_notes = [task for task in self.tasks if task.notes]
        return tasks_with_notes

    def list_recurring_tasks(self):
        recurring_tasks = [task for task in self.tasks if task.recurrence]
        return recurring_tasks

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        task.reminder = reminder_date
        self.history.append(("reminder_set", task))

    def completion_percentage(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.status == "Completed"])
        if total_tasks == 0:
            return 0.0
        return (completed_tasks / total_tasks) * 100
