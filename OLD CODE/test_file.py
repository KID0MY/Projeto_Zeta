import json

class JsonOperations:

    def __init__(self,jsonfile):
        self.jsonfile = jsonfile
        print(self.jsonfile)
    
    def ReadJson(self):
        print(self.jsonfile)
        with open(self.jsonfile, "r") as jfile:
            self.data = json.load(jfile)

    def DisplayJson(self):
        print(self.data)

    def WriteJson(self):
      with open(self.jsonfile, "w") as jfileW:
            self.write = json.dumps(newdata)  

file = JsonOperations("todo.json")

file.ReadJson()
file.DisplayJson()

"""
    def ReadJson():
        JsonFile = fjson
        f = open(JsonFile)
        data = json.load(f)
        return data


        with open('example.json', 'r') as file:
    # Load the contents of the file into a dictionary
    data = json.load(file)

"""
#    def WriteJson(self, Datajson, Wjson):
