"""uflist app.

contains a lot of hacks to create routes dynamically based on language
and based on the list of machines in machines.py

some parts might be the best or the worst code I've ever written. not sure which"""
from typing import Callable

from fastapi import Cookie, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.machines import MACHINES_EN, MACHINES_SV, Languages, Machine

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page."""
    context = dict(
        request=request,
        language=Languages.SWEDISH,
        machines=MACHINES_SV,
        current_machine=None,
    )
    return templates.TemplateResponse("home.html.j2", context)


def _build_route(machine_sv: Machine, machine_en: Machine) -> Callable:
    @app.get(f"/{machine_sv.slug}", response_class=HTMLResponse)
    async def _f(
        request: Request,
        swedish: str | None = Cookie(default="true"),
    ):
        if swedish and swedish == "true":  # can only store strings in cookies
            context = dict(
                request=request,
                language=Languages.SWEDISH,
                machines=MACHINES_SV,
                current_machine=machine_sv,
            )
        else:
            context = dict(
                request=request,
                language=Languages.ENGLISH,
                machines=MACHINES_EN,
                current_machine=machine_en,
            )
        return templates.TemplateResponse("machine.html.j2", context)

    return _f


for msv, men in zip(MACHINES_SV, MACHINES_EN):
    _f = _build_route(msv, men)
    globals()[f"{msv.slug}_page"] = _f
    del _f
