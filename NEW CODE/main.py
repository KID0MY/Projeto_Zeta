from operations import operations
from jsonoperations import JsonOperations
from title import Logo
import checkboxes
import datetime

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

jsonfile = "todo.json"

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
get_date = datetime.datetime.now()
date = get_date.strftime("%x")

op = operations(list, task, date)

fullentry = op.AddToList()  # returning list with items

Jop = JsonOperations(jsonfile, fullentry)
