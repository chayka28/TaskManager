from fastapi import FastAPI, HTTPException, status
from schemas import STaskAdd, TaskResponse
from services import create_task, get_all_tasks, get_task

app = FastAPI()

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def add_task(task: STaskAdd):
    return create_task(task.model_dump())

@app.get("/tasks", response_model=list[TaskResponse])
async def task_list():
    return get_all_tasks()

@app.get("/tasks/{id}", response_model=TaskResponse)
async def task(task_id: int):
    found = get_task(task_id)
    if not found:
        raise HTTPException(status_code=404, detail="Task not found")
    return found