"""Machines with instructions."""

from enum import Enum

from pydantic import BaseModel, HttpUrl


class Languages(str, Enum):
    """Languages used in app."""

    SWEDISH = "sv"
    ENGLISH = "en"


class Instruction(BaseModel):
    """Model for a single instruction"""

    step: int
    instruction: str

    notes: str | None = None


def create_instruction(
    step: int,
    instruction: str,
    instruction_en: str,
    notes: str | None = None,
    notes_en: str | None = None,
) -> tuple[Instruction, Instruction]:
    """Create Instructions (in two languages!)."""
    inst_sv = Instruction(step=step, instruction=instruction, notes=notes)
    inst_en = Instruction(step=step, instruction=instruction_en, notes=notes_en)
    return inst_sv, inst_en


class Machine(BaseModel):
    """Model for all machines with instructions."""

    slug: str

    name: str

    description: str

    wiki_link: HttpUrl | None = None

    setup_instructions: list[Instruction]
    teardown_instructions: list[Instruction]


def create_machine(
    slug: str,
    name: str,
    name_en: str,
    description: str,
    description_en: str,
    setup_instructions: list[tuple[Instruction, Instruction]],
    teardown_instructions: list[tuple[Instruction, Instruction]],
    wiki_link: str | None = None,
) -> tuple[Machine, Machine]:
    """Create Machine with Instructions (in two languages!)."""
    machine_sv = Machine(
        slug=slug,
        name=name,
        description=description,
        wiki_link=wiki_link,  # type: ignore
        setup_instructions=[si[0] for si in setup_instructions],
        teardown_instructions=[ti[0] for ti in teardown_instructions],
    )
    machine_en = Machine(
        slug=slug,
        name=name_en,
        description=description_en,
        wiki_link=wiki_link,  # type: ignore
        setup_instructions=[si[0] for si in setup_instructions],
        teardown_instructions=[ti[0] for ti in teardown_instructions],
    )
    return machine_sv, machine_en


laser, laser_en = create_machine(
    slug="laser",
    name="Laserskärare",
    name_en="Laser cutter",
    description="En maskin som kan skära ut saker i diverse material.",
    description_en="A machine that can cut things using a laser beam.",
    wiki_link="http://wiki.mikrofabriken.se/index.php/Bodor_Lasersk%C3%A4rare",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)

cnc_wood, cnc_wood_en = create_machine(
    slug="cnc_wood",
    name="CNC - trä",
    name_en="CNC - wood",
    description="En maskin som kan fräsa ut saker i trä.",
    description_en="A machine that can mill things in wood using a cutter.",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)

cnc_metal, cnc_metal_en = create_machine(
    slug="cnc_metal",
    name="CNC - metall",
    name_en="CNC - metal",
    description="En maskin som kan fräsa ut saker i metal.",
    description_en="A machine that can mill things in metal using a cutter.",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)

cnc_plasma, cnc_plasma_en = create_machine(
    slug="cnc_plasma",
    name="CNC - plasma",
    name_en="CNC - plasma",
    description="En maskin som kan skära saker med hjälp av plasma.",
    description_en="A machine that can cut things using a plasma beam.",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)

fdm_printer, fdm_printer_en = create_machine(
    slug="fdm_printer",
    name="FDM printer",
    name_en="FDM printer",
    description="En maskin som kan skriva ut saker i 3D.",
    description_en="A that can print things in 3D.",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)


resin_printer, resin_printer_en = create_machine(
    slug="resin_printer",
    name="Resin printer",
    name_en="Resin printer",
    description="En maskin som kan skriva ut saker i 3D.",
    description_en="A that can print things in 3D.",
    setup_instructions=[
        create_instruction(
            step=1,
            instruction="Gör det här först",
            instruction_en="Do this first",
            notes="Tänk på det här",
            notes_en="Don't forget do to verify this",
        ),
        create_instruction(
            step=2,
            instruction="Sen ska det här göras",
            instruction_en="Then do this",
            notes="Tänk också på det här",
            notes_en="Also remember this fact",
        ),
        create_instruction(
            step=3,
            instruction="Därefter måste den här saken fixas",
            instruction_en="Then you will have to do this",
        ),
        create_instruction(
            step=4,
            instruction="Sätt på maskinen",
            instruction_en="Turn on the machine!",
            notes="Akta fingrarna!",
            notes_en="Watch your fingers",
        ),
        create_instruction(
            step=5,
            instruction="Kör igång",
            instruction_en="Let's go",
            notes="Lycka till",
            notes_en="Godspeed",
        ),
    ],
    teardown_instructions=[
        create_instruction(
            step=1,
            instruction="Stäng av maskinen",
            instruction_en="Turn off the machine",
        )
    ],
)


MACHINES_SV = [laser, cnc_wood, cnc_metal, cnc_plasma, fdm_printer, resin_printer]
MACHINES_EN = [
    laser_en,
    cnc_wood_en,
    cnc_metal_en,
    cnc_plasma_en,
    fdm_printer_en,
    resin_printer_en,
]
