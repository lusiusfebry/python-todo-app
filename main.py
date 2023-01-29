import os
# from function import get_todos,write_todos
import function
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It Is", now)
is_complete = True
while is_complete:
    user_action = input("Type add, show, edit,complete or exit : ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = function.get_todos()

        todos.append(todo + "\n")
        os.system('cls')

        function.write_todos(todos)

    elif user_action.startswith("show"):
        todos = function.get_todos()

        # print (todos)
        # new_todos =[]
        # for item in todos:
        #     new_item = item.strip()
        #     new_todos.append(new_item)
        #
        # for i,j in enumerate(new_todos):
        #     print (i," ",j)

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1} |{item}")

    elif user_action.startswith("edit"):
        try:

            numbers = int(user_action[5:])
            numbers = numbers - 1
            todos = function.get_todos()

            todos[numbers] = input("Enter new todo: ") + "\n"

            function.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            numbers = int(user_action[9:])
            todos = function.get_todos()

            todos_to_remove = todos[numbers - 1]
            todos.pop(numbers - 1)

            function.write_todos(todos)

            message = f"Todo {todos_to_remove.strip()} is completed and removed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        is_complete = False
    else:
        print("command not valid")
        is_complete = False

print("Bye")
