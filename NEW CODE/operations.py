class operations:

    def __init__(self, list, task, date):
        self.list = list
        self.task = task
        self.date = date

    def AddToList(self):
        self.list.append(self.task)
        self.list.append(self.date)
        print("list = ", self.list, "\nTask =", self.task,"\nDate =", self.date)
