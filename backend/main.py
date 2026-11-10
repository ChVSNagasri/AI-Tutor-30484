from fastapi import FastAPI

klu=FastAPI(title="AI Tutor",
            description="AI Tutor PBL Project",
            version="1.0.0"
            )

@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message": "KL University"}


@klu.get("/askquestion")
def ask():
    return {"message": "What is LLM","Answer":"Long Language Model"}


@klu.get("/student")
def student():
    return {"id":1,"name":"Ram","gender":"male","course":"DSA"}


@klu.get("/students")
def getstudents():
    return [
        {"id":1,"name":"Nagasri","gender":"female","course":"DSA"},
        {"id":2,"name":"Sri","gender":"female","course":"DSA"},
        {"id":3,"name":"Sruthi","gender":"female","course":"DSA"}
    ]
        



