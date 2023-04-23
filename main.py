# To-DO PRoject
# ━━━━━━━<Bibliotecas>━━━━━━━━━━ #

import colorama
import datetime
import json

from colorama import Fore

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

list = []
fjson = "todo.json"
newdata = None
checkbox = Fore.WHITE + "[" + Fore.RED + 'x' + Fore.WHITE + "]"

# ━━━━━━━━━━━<Classes>━━━━━━━━━━ #


class operations:
    # list operations

    def add(taskname, date):
        list.append(taskname)
        list.append(date)

    def transmit(data):
        data = list
        return data

class JsonOperations:
    # Json Operations(Working on it)
    def __init__(self,jsonfile):
        self.jsonfile = jsonfile
        print(self.jsonfile)
    
    def ReadJson(self):
        print(self.jsonfile)
        with open(self.jsonfile, "r") as jfile:
            self.data = json.load(jfile)
            print(self.data)

    def DisplayJson(self):
        print(self.data)

    def WriteJson(self):
      with open(self.jsonfile, "w") as jfileW:
            self.write = json.dumps(newdata)  

# ━━━━━━━<Codigo Bruto>━━━━━━━━━ #

#get task & date
Add_task = input("Task name: ")
get_date = datetime.datetime.now()

#add task & date to list
operations.add(Add_task, get_date.strftime("%x"))
newdata = operations.transmit(newdata)

file = JsonOperations("todo.json")
file.ReadJson()
file.WriteJson()
file.DisplayJson()


print(checkbox, newdata)

