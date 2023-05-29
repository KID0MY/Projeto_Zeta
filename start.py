from options import comecar
import checkboxes
import jsonoperations
# ━━━━━━━━━━<Variaveis>━━━━━━━━━ #
jsonfile = "todo.json"
opt = comecar(jsonfile)

# ━━━━━━━━━━━<Funções>━━━━━━━━━━━ #
def Logo():
    print("===================================================================================\n")
    print("$$$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\          $$\       $$$$$$\  $$$$$$\ $$$$$$$$\ \n\__$$  __|$$  __$$\ $$  __$$\ $$  __$$\         $$ |      \_$$  _|$$  __$$\\__$$  __|\n   $$ |   $$ /  $$ |$$ |  $$ |$$ /  $$ |        $$ |        $$ |  $$ /  \__|  $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$\ $$ |        $$ |  \$$$$$$\    $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |\______|$$ |        $$ |   \____$$\   $$ |   \n   $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |        $$ |        $$ |  $$\   $$ |  $$ |   \n   $$ |    $$$$$$  |$$$$$$$  | $$$$$$  |        $$$$$$$$\ $$$$$$\ \$$$$$$  |  $$ |   \n   \__|    \______/ \_______/  \______/         \________|\______| \______/   \__|   ")
    print("\nAn Open Source project by: Lucas Triboli Bujes")
    print("===================================================================================")

def Options():
    print("What are we doing today? \n1.Add new task \n2.See tasks \n3.Delete task \n4.Exit \n")
    Action = int(input(">> "))

    if Action == 1:
        print(checkboxes.checkbox_good, "Status = Working\n")
        opt.NewTask()
        Options()
    elif Action == 2:
        print(checkboxes.checkbox_wait, "Status = In Progress\n")
        opt.PrintUsersTodo()
        Options()
    elif Action == 3:
        opt.DeleteTask()
        Options()
    elif Action == 4:
        quit()
    else:
        print(checkboxes.checkbox_bad + " Invalid input")
        print("=====================")
        Options()