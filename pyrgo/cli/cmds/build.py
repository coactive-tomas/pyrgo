"""Build command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.cmds._utils import inform_and_run_program
from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf


@click.command("build")
def build() -> None:
    """Build project with `build`."""
    program_execution = inform_and_run_program(
        commands=[
            PythonCommandExec.new(
                program="build",
            ).add_args(
                [PyrgoConf.new().cwd.as_posix()],
            ),
        ],
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
