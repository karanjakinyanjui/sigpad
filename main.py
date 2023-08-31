from nicegui import ui, app
from fastapi.responses import RedirectResponse
from typing import Callable, Optional
from nicegui.element import Element
import sqlite3
import datetime

primary_color = "green"


class Pad(Element, component="psign.js"):
    def __init__(
        self,
        title: str,
        *,
        on_change: Optional[Callable] = None,
        on_close: Optional[Callable] = None,
    ) -> None:
        super().__init__()
        self.on("change", on_change)
        self.on("close", on_close)

    def reset(self) -> None:
        self.run_method("reset")


@ui.page("/")
def confirm_delivery():
    with ui.header(fixed=False).style(f"background-color: {primary_color};"):
        with ui.row().style("align-items: center; text-align: center;"):
            ui.label("Freight Forever").style("font-size: 25px; font-weight: bold;")

            with ui.element("div").classes("max-[750px]:hidden"):
                ui.link("Confirm Delivery", target="/").style(
                    "margin-left: 500px; font-size: 20px;"
                ).classes(replace="text-lg text-white")
                ui.link("Upload Documents", target="/upload_document").style(
                    "margin-left: 30px; font-size: 20px;"
                ).classes(replace="text-lg text-white")
                ui.link("View Documents", target="/view_documents").style(
                    "margin-left: 30px; font-size: 20px;"
                ).classes(replace="text-lg text-white")
                ui.link("Log Out", target="/login").style(
                    "margin-left: 30px; font-size: 20px;"
                ).classes(replace="text-lg text-white")

            with ui.button(icon="menu", color="white").style(
                f"position: absolute; right: 20px; color: {primary_color};"
            ).classes("min-[751px]:hidden"):
                with ui.menu() as menu:
                    ui.menu_item("Confirm Delivery", on_click=lambda: ui.open("/"))
                    ui.menu_item(
                        "Upload Documents", on_click=lambda: ui.open("/upload_document")
                    )
                    ui.menu_item(
                        "View Documents", on_click=lambda: ui.open("/view_documents")
                    )
                    ui.menu_item("Logout")
                    ui.separator()
                    ui.menu_item("Close", on_click=menu.close)

    ui.label("Confirm Delivery").style(
        f"color: {primary_color}; font-size: 30px; font-weight: bold; margin-left: auto; margin-right: auto;"
    )

    document_options = (
        ui.select(
            options=["test", "test1", "test2"], label="Choose An Uploaded Document"
        )
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )

    status_options = (
        ui.select(
            ["Open", "Delivered", "Delivery With Issues", "Delivery Rejected"],
            label="Delivery Status",
            value="Open",
        )
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    item_name = (
        ui.input(label="Item Name")
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    quantity = (
        ui.input(label="Quantity", value=1)
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    date = (
        ui.input(label="Date", value=datetime.date.today())
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    customer_address = (
        ui.input(label="Customer Address")
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    ui.select(["Yes", "No"], label="Discrepancies").style(
        "width: 320px; margin-left: auto; margin-right: auto;"
    ).props('outlined color="emerald-500"')
    comments = (
        ui.textarea(label="Comments")
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )

    def handleSignature(signature):
        print(signature)

    def get_signature():
        with ui.dialog(value=True) as signature_dialog:
            signature_dialog.props("")
            with ui.card().tight():
                Pad(
                    "Clicks",
                    on_change=lambda e: handleSignature(signature=e.args),
                    on_close=signature_dialog.close,
                )

    ui.label("Signature").style(
        f"color: {primary_color}; font-size: 30px; font-weight: bold; margin-left: auto; margin-right: auto;"
    )
    print_name = (
        ui.input("Print Name")
        .style("width: 320px; margin-left: auto; margin-right: auto;")
        .props('outlined color="emerald-500"')
    )
    sig_button = ui.button(
        "Get Signature", on_click=lambda: get_signature(), color=primary_color
    ).style("color: white; margin-left: auto; margin-right: auto;")


ui.run(storage_secret="secret", title="test", port=8000)
