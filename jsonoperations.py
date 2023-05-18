import json

class JsonOperations:
    # ━━━━━━━━━━|Initiate Class|━━━━━━━━━━━ #
    def __init__(self, jsonfile):  # initialize Json Stuff
        self.jsonfile = jsonfile
        with open(self.jsonfile, "r") as fjson:
            self.data = json.load(fjson)
    
    
    # ━━━━━━━━━━━━|Get User|━━━━━━━━━━━━━━━ #
    def GetUsers(self):
        users = list(self.data.keys())
        print("Users:")
        x = 1
        for user in users:
            print(x,"- ",user)
            x += 1

    #━━━|Get the DATA from the USER to put in the json|━━━#
    def GetJsonData(self, task, date): # get old data + new data
        self.task_name = task
        self.date = date


    def WriteJson(self, user_id, status):
        task = {
            "task_name": self.task_name,
            "status": status,
            "date": self.date
        }
        if user_id in self.data:
            # append the new task to the existing user's task list
            self.data[user_id].append(task)
        else:
            # create a new task list for the user and add the new task
            self.data[user_id] = [task]
        
        #Dump the info inside the Json
        with open(self.jsonfile, "w") as fjson:
            json.dump(self.data, fjson)

        print(f"Added task '{self.task_name}' for user {user_id} with status '{status}'")

    def PrintJsonList(self): # get old data + new data
        user_id = "kidomy"
        if user_id in self.data:
            tasks = data[user_id]
            for task in tasks:
                print(f"Task name: {task['task_name']}")
                print(f"Status: {task['status']}")
                print(f"Date: {task['date']}")
                print("\n")