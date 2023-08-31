#!/usr/bin/env python3
from pad import Pad

from nicegui import ui


def handleSignature(signature):
    print(signature)


with ui.dialog() as dialog, ui.card():
    dialog.props("persistent")
    counter = Pad(
        "Clicks",
        on_change=lambda e: handleSignature(signature=e.args),
        on_close=dialog.close,
    )


ui.button("Dialog", on_click=dialog.open)


ui.button("Reset", on_click=counter.reset).props("small outline")

ui.run(host="0.0.0.0")
