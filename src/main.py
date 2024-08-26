from fastapi import FastAPI
from src.routes import home, hacker_news

app = FastAPI()


app.include_router(home.router)
app.include_router(hacker_news.router)
