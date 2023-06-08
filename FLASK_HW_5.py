from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


class Task8(BaseModel):
    id: int
    title: str
    description: str
    status: bool


app = FastAPI()


tasks = []


@app.get("/all_tasks/", response_model=List[Task8])
def get_all_tasks():
    return tasks


@app.get("/task/{task_id}", response_model=List[Task8])
def get_task(task_id: int):
    new_list = []
    for obj in tasks:
        if obj.id == task_id:
            new_list.append(obj)
    if new_list:
        return new_list
    else:
        raise HTTPException(status_code=404, detail=f"Task_not_found")


@app.post("/post_tasks/", response_model=Task8)
def post_tasks(task: Task8):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


@app.put("/put_task/{task_id}", response_model=Task8)
def put_tasks(new_task: Task8, task_id: int):
    for i, obj in enumerate(tasks):
        if obj.id == task_id:
            tasks[obj] = new_task
            return new_task
    raise HTTPException(status_code=404, detail=f"Task_not_found")


@app.delete("/delete_task/{task_id}", response_model=Task8)
def delete_tasks(task_id: int):
    for i, obj in enumerate(tasks):
        if obj.id == task_id:
            return tasks.pop(i)
    raise HTTPException(status_code=404, detail=f"Task_not_found")