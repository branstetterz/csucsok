from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# statikus fájlok (CSS)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/sounds", StaticFiles(directory="sounds"), name="sounds")

# HTML template-ek
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
