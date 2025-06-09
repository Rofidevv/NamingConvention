from command_interface import Command

class AddTaskCommand(Command):
    def __init__(self, todo_list, task):
        self.todo_list = todo_list
        self.task = task

    def execute(self):
        self.todo_list.add_task(self.task)

    def undo(self):
        self.todo_list.remove_task(len(self.todo_list.tasks) - 1)


class RemoveTaskCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index
        self.removed_task = None

    def execute(self):
        self.removed_task = self.todo_list.remove_task(self.index)

    def undo(self):
        self.todo_list.tasks.insert(self.index, self.removed_task)


class MarkAsDoneCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index

    def execute(self):
        self.todo_list.mark_done(self.index)

    def undo(self):
        self.todo_list.mark_undone(self.index)
