# To-DO PRoject
# ━━━━━━━<Bibliotecas>━━━━━━━━━━ #

import colorama
import datetime
import json

from colorama import Fore

# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #

list = []
newdata = None
fjson = "todo.json"
checkbox_bad = Fore.WHITE + "[" + Fore.RED + 'x' + Fore.WHITE + "]"
checkbox_good = Fore.WHITE + "[" + Fore.GREEN + 'o' + Fore.WHITE + "]"
checkbox_wait = Fore.WHITE + "[" + Fore.YELLOW + '-' + Fore.WHITE + "]"

# ━━━━━━━━━━━<Classes>━━━━━━━━━━ #
def checkbox_status():
    if data == None:
        checkbox = Fore.WHITE + "[" + Fore.RED + 'x' + Fore.WHITE + "]"
    else:
        checkbox = Fore.WHITE + "[" + Fore.GREEN + 'o' + Fore.WHITE + "]"
    return checkbox

class operations:
    # list operations

    def add(taskname, date):
        print(checkbox_good, "-> operations.add in work")
        list.append(taskname)
        list.append(date)

    def transmit(data):
        print(checkbox_good, "-> operations.transmit in work")
        data = list
        return data

class JsonOperations:
    # Json Operations(Working on it)
    def __init__(self,jsonfile):
        print(checkbox_good, "-> JsonOperations.init in work")
        self.jsonfile = jsonfile
        data = operations.transmit(newdata)
        print("The Json File is: ", self.jsonfile, "and data = ", data) # it is working

    #fix bug 
    def ReadJson(self):
        print(checkbox_good, "-> JsonOperations.ReadJson in work")
        try:
            with open(self.jsonfile, "r") as jfile:
                self.data = json.load(jfile)
                print(self.data)
        except json.decoder.JSONDecodeError as e:
            print(checkbox_bad, "Error: Invalid JSON syntax in the file:", self.jsonfile)
            print(checkbox_wait, "Adding default data to the file...")
            with open(self.jsonfile, "w") as jfile:
                self.write = json.dumps("{}")
                self.data = {}

    def DisplayJson(self):
        print(checkbox_good, "-> JsonOperations.DisplayJson in work")
        print("DATA in file =", self.data)

    def WriteJson(self, data):
        print(checkbox_good, "-> JsonOperations.WriteJson in work")
        print("this data will be written in the .json file:", data)
        self.fdata = data
        with open(self.jsonfile, "w") as jfileW:
            jfileW.write(json.dumps(self.fdata))
            print("Data Dumped")
        self.data = self.fdata

# ━━━━━━━<Codigo Bruto>━━━━━━━━━ #

#get task & date
Add_task = input("Task name: ")
get_date = datetime.datetime.now()

#add task & date to list
operations.add(Add_task, get_date.strftime("%x"))
data = operations.transmit(newdata)
print("DATA =", data)

file = JsonOperations("todo.json")
file.ReadJson()
print("NEWDATA = ", data)
file.WriteJson(data)
file.DisplayJson()


print(checkbox_status(), data)

