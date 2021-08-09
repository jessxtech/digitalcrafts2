todo_list = ["learn python", "study", "eat better"]
            # 0, 1, 2
            #-1, -2, -3

# print(todo_list[0])

# print(todo_list[-1])

# try:
#    print(todo_list[1])
# except IndexError:
#    print("That item does not exist")

# print(todo_list[2])

todo_list = ["learn python", "study", "eat better", "sleep","become engineer","walk dog"]

# print(todo_list[-2:])

# index = 0
# count = index + 1

# while index < len(todo_list):
#    todo = todo_list[index]
#    print("You need to do this:" + str(count), todo)
#    index = index + 1
#    count = count + 1

for item in todo_list:
    print(item)