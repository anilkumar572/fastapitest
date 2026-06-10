from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome Anil, this is your first backend deployment!"
    }

@app.get("/about")
def about():
    return {
        "name": "Anil Kumar",
        "role": "Software Developer",
        "status": "Learning Cloud Deployment"
    }
