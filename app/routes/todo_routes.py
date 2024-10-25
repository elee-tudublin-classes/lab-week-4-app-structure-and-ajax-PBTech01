from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import service functions
from app.services.todo_service import getAllTodos, addTodo

router = APIRouter()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the todos page
@router.get("/", response_class=HTMLResponse)
async def todos(request: Request):

    # note passing of parameters to the page
    return templates.TemplateResponse("todos.html", {"request": request, "todoList": getAllTodos() })

@router.post("/add")
def add_item(request: Request, item: str = Form(...)):

    # get item value from the form POST data
    new_todo : str = addTodo(item)
    return templates.TemplateResponse("partials/todo/todo_li.html", {"request": request, "todo": new_todo})