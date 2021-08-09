print("To Do List")

toDoList =[]
user = ""


print("Press 1 to add a task")
print("Press 2 to delete a task")
print("Press 3 to view all tasks")
print("Press q to quit")
print("Choose priority level : high, medium, low")

while user != "q":
    user = input ("Choose an option:")
if user == "1":
    task = input("Task name:")
    priority = input("Choose a priority level:")
    print(task + " - " + priority)
    toDoList.append(task + " - " + priority)
    print(toDoList)

elif user == "2":
    count = 0
    for todo in toDoList:
        print("%d: %s" % (count,todo))
        count += 1
    delTask = input("Choose which option to delete:")
    del toDoList[int(delTask)]
    print(toDoList)

elif user == "3":
    taskDict = {}
    taskDict = toDoList
    print(taskDict)
    count = 1
    for todo in toDoList:
        print("%d - %s" % (count, todo))
        count +=1

elif user == "q":
    print("End of task list")
    