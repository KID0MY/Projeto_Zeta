# To-DO PRoject
# ━━━━━━━<Bibliotecas>━━━━━━━━━━ #
from operations import operations
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

class JsonOperations:
    # Json Operations(Working on it)
    def __init__(self,jsonfile): #initialize Json Stuff
        print(checkbox_good, "-> JsonOperations.init in work")
        self.jsonfile = jsonfile
        data = operations.transmit(newdata)
        self.oldata = None
        self.retornoj = None
        print("The Json File is: ", self.jsonfile, "and data = ", data) # it is working

    def CheckJson(self): #get old data + new data
        print(checkbox_good, "-> JsonOperations.CheckJson in work")
        print("The variables are:", self.oldata, "and", self.fdata)
        if self.oldata == None:
            retornoj = self.fdata
        else:
            retornoj = self.oldata, self.fdata
        return retornoj

    def ReadJson(self):
        print(checkbox_good, "-> JsonOperations.ReadJson in work")
        try:
            with open(self.jsonfile, "r") as jfile:
                self.data = json.load(jfile)
                self.oldata = self.data
                print(self.data)
        #se o json tiver errado, zerar ele
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
            jfileW.write(json.dumps(self.CheckJson()))
            print("Data Dumped")
        self.data = self.fdata

# ━━━━━━━<Codigo Bruto>━━━━━━━━━ #

#send list to class
operations(list)

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
