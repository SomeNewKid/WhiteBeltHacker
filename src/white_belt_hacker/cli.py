"""Command-line interface for the application."""

from __future__ import annotations

import asyncio

from white_belt_hacker.agent import run_agent


def main() -> int:
    """Run the command-line interface."""
    exit_code = asyncio.run(run_agent())
    return exit_code
