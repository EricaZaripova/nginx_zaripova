from typing import Optional

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "number": None })


@app.get("/{number}")
def main_get(request: Request, number: int):
    return templates.TemplateResponse("index.html", {"request": request, "number": number})


if __name__ == "main":
    uvicorn.run(app)
