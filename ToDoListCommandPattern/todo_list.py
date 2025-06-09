class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def remove_task(self, index):
        return self.tasks.pop(index)

    def mark_done(self, index):
        self.tasks[index]["done"] = True

    def mark_undone(self, index):
        self.tasks[index]["done"] = False

    def show_tasks(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["done"] else "✗"
                print(f"{i+1}. [{status}] {task['task']}")