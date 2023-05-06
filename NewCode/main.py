from jsonoperations import JsonOperations
from title import Logo
import checkboxes
import datetime
import os

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

jsonfile = "NewCode/todo.json"

list = []

# ━━━━━━━━━━━<Classes>━━━━━━━━━━ #


def checkbox_status():
    if data == None:
        checkbox.checkbox_bad
    else:
        checkbox.checkbox_good
    return checkbox

# ━━━━━━━<Codigo Bruto>━━━━━━━━━ #

Logo()

task = input("Task name: ")
date = (datetime.datetime.now()).strftime("%x")
#date = get_date.strftime("%x")

Jop = JsonOperations(jsonfile, task, date)
Jop.CheckJson()
Jop.WriteJson("kidomy", "pending")