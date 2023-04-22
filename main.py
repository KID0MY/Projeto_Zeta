#To-DO PRoject
#━━━━━━━<Bibliotecas>━━━━━━━━━━

import colorama
import datetime
import json

from colorama import Fore

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

list = []
fjson = "todo.json"

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class operations:
#list operations
    def add(taskname, date):
        taskname = taskname
        date = date
        list.append(taskname)
        list.append(date)

class JsonOp:
# Json Operations    
    def OpenJson(fjson):
        JsonFile = fjson
        f = open(JsonFile)
        data = json.load(f)
        return data

    def WriteJson(Datajson, Wjson):
        Datajson = data
        with open(fjson, 'w') as outfile:
            json.dump(json_string, outfile)


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
checkbox = Fore.WHITE + "[" + Fore.RED + 'x' + Fore.WHITE + "]"

Add_task = input("Task name: ")
get_date = datetime.datetime.now()

operations.add(Add_task,get_date.strftime("%x"))


print(checkbox, list)

print(JsonOp.OpenJson())