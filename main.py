from jsonoperations import JsonOperations
import start
import checkboxes
import datetime

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

jsonfile = "todo.json"

list = []

# ━━━━━━━━━━━<Funções>━━━━━━━━━━━ #

def checkbox_status():
    if data == None:
        checkbox.checkbox_bad
    else:
        checkbox.checkbox_good
    return checkbox

# ━━━━━━━━━━<Codigo>━━━━━━━━━━━ #

start.Logo()
start.Options()

task = input("Task name: ")
date = (datetime.datetime.now()).strftime("%x")
#date = get_date.strftime("%x")

Jop = JsonOperations(jsonfile)
Jop.GetJsonData(task, date)

Jop.WriteJson("kidomy", "pending")