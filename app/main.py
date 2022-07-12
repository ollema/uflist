"""uflist app.

contains a lot of hacks to create routes dynamically based on language
and based on the list of machines in machines.py

some parts might be the best or the worst code I've ever written. not sure which"""
from typing import Callable, Union

from fastapi import Cookie, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.machines import MACHINES_EN, MACHINES_SV, Languages, Machine

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    swedish: Union[str, None] = Cookie(default=None),
):
    """Home page."""
    if swedish and swedish == "true":  # can only store strings in cookies
        selected_language = Languages.SWEDISH
    else:
        selected_language = Languages.ENGLISH

    context = dict(
        request=request,
        language=selected_language,
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
            selected_language = Languages.SWEDISH
            selected_machine = machine_sv
            selected_machines = MACHINES_SV
        else:
            selected_language = Languages.ENGLISH
            selected_machine = machine_en
            selected_machines = MACHINES_EN

        context = dict(
            request=request,
            language=selected_language,
            machines=selected_machines,
            current_machine=selected_machine,
        )
        return templates.TemplateResponse("machine.html.j2", context)

    return _f


for msv, men in zip(MACHINES_SV, MACHINES_EN):
    _f = _build_route(msv, men)
    globals()[f"{msv.slug}_page"] = _f
    del _f
