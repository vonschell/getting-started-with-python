todo_list = []
done = False

print("Type 'done' at any time to exit")

#Create a while loop that is set to not done
while not done:
    new_item = input("Add an item to the to-do list here: ")

    if new_item == "done":
        done = True
    else:
        todo_list.append(new_item)

print(todo_list)
