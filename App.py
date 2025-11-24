from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Label, Button


class Menu(App):
    CSS_PATH = "utility_containers.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="column"):
                yield Static("One", classes="box")
                yield Static("Two", classes="box")
            with Vertical(classes="column"):
                yield Static("Three", classes="box")
                yield Static("Four", classes="box")

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = Menu()
    app.run()