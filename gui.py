import function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box  = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app",
                   layout=[[label],
                           [input_box,add_button]],
                   font=("helvetica",15))
while True:
    event,values = window.read()
    print(event)
    print(values)
    print(type(values))
    match event:
        case "Add" :
            todos = function.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            function.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()