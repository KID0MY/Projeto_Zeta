import checkboxes
import jsonoperations

def Logo():
    print("===================================================================================\n")
    print("$$$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\          $$\       $$$$$$\  $$$$$$\ $$$$$$$$\ \n\__$$  __|$$  __$$\ $$  __$$\ $$  __$$\         $$ |      \_$$  _|$$  __$$\\__$$  __|\n   $$ |   $$ /  $$ |$$ |  $$ |$$ /  $$ |        $$ |        $$ |  $$ /  \__|  $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$\ $$ |        $$ |  \$$$$$$\    $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |\______|$$ |        $$ |   \____$$\   $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |        $$ |        $$ |  $$\   $$ |  $$ |   \n   $$ |    $$$$$$  |$$$$$$$  | $$$$$$  |        $$$$$$$$\ $$$$$$\ \$$$$$$  |  $$ |   \n   \__|    \______/ \_______/  \______/         \________|\______| \______/   \__|   ")
    print("\nAn Open Source project by: Lucas Triboli Bujes")
    print("===================================================================================")

def Options():
    print("What are we doing today? \n1.Add new task \n2.See tasks \n3.Delete task \n")
    Action = int(input(">> "))

    if Action == 1:
        pass
    elif Action == 2:
        pass 
    elif Action == 3:
        pass
    else:
        print(checkboxes.checkbox_bad + " Invalid input")
        print("=====================")
        Options()