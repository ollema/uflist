"""uflist app."""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.machines import (
    MACHINES_SV,
    Languages,
    cnc_metal,
    cnc_plasma,
    cnc_wood,
    fdm_printer,
    laser,
    resin_printer,
)

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


for machine in MACHINES_SV:

    @app.get(f"/{machine.slug}", response_class=HTMLResponse)
    async def _f(request: Request):
        context = dict(
            request=request,
            language=Languages.SWEDISH,
            machines=MACHINES_SV,
            current_machine=machine,
        )
        return templates.TemplateResponse("machine.html.j2", context)

    globals()[f"{machine.slug}_page"] = _f

    del _f


# @app.get("/laser", response_class=HTMLResponse)
# async def laser_page(request: Request):
#     """Laser cutter page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=laser,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)


# @app.get("/cnc_wood", response_class=HTMLResponse)
# async def cnc_wood_page(request: Request):
#     """CNC - wood page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=cnc_wood,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)


# @app.get("/cnc_metal", response_class=HTMLResponse)
# async def cnc_plastics_page(request: Request):
#     """CNC - metal page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=cnc_metal,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)


# @app.get("/cnc_plasma", response_class=HTMLResponse)
# async def cnc_plasma_page(request: Request):
#     """CNC - plasma page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=cnc_plasma,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)


# @app.get("/fdm_printer", response_class=HTMLResponse)
# async def fdm_printer_page(request: Request):
#     """FDM printer page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=fdm_printer,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)


# @app.get("/resin_printer", response_class=HTMLResponse)
# async def resin_printer_page(request: Request):
#     """Resin printer page."""
#     context = dict(
#         request=request,
#         language=Languages.SWEDISH,
#         machines=MACHINES_SV,
#         current_machine=resin_printer,
#     )
#     return templates.TemplateResponse("machine.html.j2", context)
