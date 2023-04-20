#To-DO PRoject
from fuctions import operations
import colorama
import datetime
from colorama import Fore
from datetime import date


Add_task = input("Task name: ")

get_date = date.today()

operations.add(Add_task,get_date)

print(operations.list)