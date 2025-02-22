# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos):
   
    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
       print("Todo is not in list!")

  # Creating a get_todos() function
  def get_todos(self):
    return self.todos

  # Creating a get_birthday function
  def get_birthday(self, name):
    if name == "Kirby":
      print("Birthday is 03/10/97!")
    elif name == "Jade":
      print("Birthday is 11/23/98")
    elif name == "Amy":
      print("Birthday is 12/20/97")
    else:
      print("Can't find a birthday for this person...")

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There is no contact with the name you inserted!"


# Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")

# print(assistant.get_todos())
# print(assistant.get_contact("Chelsea"))
# print(assistant.get_birthday("Kirby")) 