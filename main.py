from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(
    title="Anil's First API",
    description="My first deployed FastAPI application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------
# Models
# ----------------------

class Task(BaseModel):
    title: str
    completed: bool = False


tasks = []

# ----------------------
# Existing Endpoints
# ----------------------

@app.get("/")
def home():
    return {
        "message": "Welcome Anil, this is your first backend deployment!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/about")
def about():
    return {
        "name": "Anil Kumar Doppalapudi",
        "role": "Software Developer",
        "skills": [
            "Flutter",
            "FastAPI",
            "Python",
            "Firebase",
            "Next.js",
            "Dart"
        ]
    }


@app.get("/time")
def get_time():
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/quote")
def random_quote():
    quotes = [
        "Keep building.",
        "Consistency beats motivation.",
        "Small steps every day.",
        "Learn. Build. Repeat.",
        "Your next project can change your life."
    ]

    return {
        "quote": random.choice(quotes)
    }


@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b
    }


@app.get("/profile/{username}")
def profile(username: str):
    return {
        "username": username,
        "status": "active"
    }


# ----------------------
# CRUD Operations
# ----------------------

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    if task_id >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    if task_id >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tasks[task_id] = task

    return {
        "message": "Task updated",
        "task": task
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id >= len(tasks):
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }
