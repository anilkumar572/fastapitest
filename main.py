from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(
    title="Anil's First API",
    description="My first deployed FastAPI application",
    version="1.0.0"
)



@app.get("/")
def home():
    return {
        "message": "Welcome Anil, this is your first backend deployment!"
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
            "Next.js"
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
