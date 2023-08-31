from typing import Callable, Optional

from nicegui.element import Element


class Pad(Element, component="signhere12.js"):
    def __init__(
        self,
        title: str,
        *,
        on_change: Optional[Callable] = None,
        on_close: Optional[Callable] = None
    ) -> None:
        super().__init__()
        self._props["title"] = title
        self.on("change", on_change)
        self.on("close", on_close)

    def reset(self) -> None:
        self.run_method("reset")
