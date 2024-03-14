import sys
sys.path.append('/home/itay/my_chat_gpt/app')
from fastapi import FastAPI, HTTPException
from backend.login.aux import login_user
from backend.Questions.aux import get_chatgpt_response
from backend.Questions.model import Question, Response
from backend.register.aux import register_user
from backend.register.model import User

app = FastAPI()

@app.post("/ask")
async def ask_question(question: Question):
    if question.text.startswith("MATH:"):
        # Handle math question
        response_text = await get_chatgpt_response(question.text[5:])
        response_model = Response(response=response_text)
        return response_model
    elif question.text.startswith("GENERAL:"):
        # Handle general question
        response_text = await get_chatgpt_response(question.text[8:])
        response_model = Response(response=response_text)
        return response_model
    else:
        response = "Invalid question format"
        return {"response": response}
    
@app.post("/register/")
async def register(username: str, password: str):
    user = User(username=username, password=password)
    if register_user(user):
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=400, detail="Unable to register user")

@app.post("/login/")
async def login(username: str, password: str):
    if login_user(username, password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
