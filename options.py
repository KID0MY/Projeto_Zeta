from jsonoperations import JsonOperations
import checkboxes
import datetime

# ━━━━━━━━━━<Codigo>━━━━━━━━━━━ #


# ━━━━━━━━━━<Classe>━━━━━━━━━━━ #
class comecar:
    def __init__(self, jsonf):
        self.jsonf = jsonf
        self.Jop = JsonOperations(jsonf)

    def NewTask(self):
        self.ChooseUser()
        task = input("Task name: ")
        date = (datetime.datetime.now()).strftime("%x")
        self.Jop.GetJsonData(task, date)
        self.Jop.WriteJson(self.usertry, "pending")

    def ChooseUser(self):
        self.Jop.GetUsers()
        self.usertry = input("What is the user of this entry?: ")




    def PrintTask(self):
        print(self.jsonf)

    def DeleteTask(self):
        print()
