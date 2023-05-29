from jsonoperations import JsonOperations
import checkboxes
import datetime

# ━━━━━━━━<variavies>━━━━━━━━━━━ #

selected_user = None

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
        selected_user = self.Jop.GetUsers()
        if selected_user is not None:
            self.usertry = selected_user
            print("User selected:", self.usertry)
        else:
            print("No user selected.")

    def PrintUsersTodo(self):
        self.Jop.PrintJsonList()


    def PrintTask(self):
        print(self.jsonf)

    def DeleteTask(self):
        print()
