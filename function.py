FILE_PATH = "todos.txt"

def get_todos(file_path=FILE_PATH):
    """ Read a text file and return the list of
    todos item
    """
    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILE_PATH):
    """
    Write the todo items list in the text file
    """
    with open(file_path, mode="w") as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print("hello")
    print(get_todos())