import function
import PySimpleGUI as sg
import time


sg.theme("GreenTan")
clock = sg.Text("",key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=function.get_todos(), key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
compete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do app",
                   layout=[[clock],
                       [label],
                           [input_box, add_button],
                           [list_box, edit_button, compete_button],
                           [exit_button]
                           ],
                   font=("helvetica", 15))
while True:
    event, values = window.read(timeout=200)
    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            function.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todos = values["todo"]
                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todos
                function.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select and an item first", font=("helvetica", 15))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select and an item first", font=("helvetica", 15))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
