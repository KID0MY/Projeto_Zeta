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
        self.Jop.GetUsers()
        task = input("Task name: ")
        date = (datetime.datetime.now()).strftime("%x")
        self.Jop.GetJsonData(task, date)
        self.Jop.WriteJson("kidomy", "pending")

    def PrintTask():
        print()

    def DeleteTask():
        print()
