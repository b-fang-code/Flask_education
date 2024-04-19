# Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять,
# удалять и получать список задач.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Task с полями id, title, description и status.
# ● Создайте список tasks для хранения задач.
# ● Создайте маршрут для получения списка задач (метод GET).
# ● Создайте маршрут для создания новой задачи (метод POST).
# ● Создайте маршрут для обновления задачи (метод PUT).
# ● Создайте маршрут для удаления задачи (метод DELETE).
# ● Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None


@app.get('/')
async def get_tasks():
    global tasks
    logger.info('Get tasks')
    return {"tasks": tasks}


@app.post('/')
async def create_task(task: Task):
    global tasks
    logger.info('Create task')
    tasks.append(task)
    return {"task": task}


@app.put('/{task_id}')
async def update_task(task_id: int, task: Task):
    global tasks
    logger.info('Update task')
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
            return {"task": task}
    return {"error": "Task not found"}


@app.delete('/{task_id}')
async def delete_task(task_id: int):
    global tasks
    logger.info('Delete task')
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}
