from colorama import Fore

checkbox_bad = Fore.WHITE + "[" + Fore.RED + 'x' + Fore.WHITE + "]"
checkbox_good = Fore.WHITE + "[" + Fore.GREEN + 'o' + Fore.WHITE + "]"
checkbox_wait = Fore.WHITE + "[" + Fore.YELLOW + '-' + Fore.WHITE + "]"

class operations:
    # list operations
    def __init__(self, list):
        self.list = list

    def add(taskname, date):
        print(checkbox_good, "-> operations.add in work")
        add = taskname + "," + date
        AddToList()

    def AddToList(self):
        self.list.append(add)
        print(add)

    def transmit(data):
        print(checkbox_good, "-> operations.transmit in work")
        data = self.add
        return data