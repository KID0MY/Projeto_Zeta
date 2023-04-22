import json

class JsonOperations:
# Json Operations
    def ReadJson(self,shouldOpen):
        if shouldOpen == True:
            with open("todo.json", "r") as jsonfile:
                self.data = json.load(jsonfile)
        print(data)

    def WriteJson(self,NewData):
        print(self.data)
    

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
JsonOperations.ReadJson(True)