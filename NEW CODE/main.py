from operations import operations
import checkboxes
import datetime

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

list = []

# ━━━━━━━━━━━<Classes>━━━━━━━━━━ #
def checkbox_status():
    if data == None:
        checkbox.checkbox_bad
    else:
        checkbox.checkbox_good
    return checkbox
    
# ━━━━━━━<Codigo Bruto>━━━━━━━━━ #

task = input("Task name: ")
get_date = datetime.datetime.now()
date = get_date.strftime("%x")

op = operations(list, task, date)

op.AddToList()