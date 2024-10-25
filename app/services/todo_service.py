# import service functions
from app.data_access.todo_dba import dataGetTodoList, dataAddTodo

# get list of todos from data
def getAllTodos() :
    return dataGetTodoList()

# add new todo using data access
def addTodo(item : str) :    
    # add todo to the list (via dataaccess)
    new_todo = dataAddTodo(item)

    # return new todo
    return new_todo