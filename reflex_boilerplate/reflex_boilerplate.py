"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from reflex_boilerplate.dashboard_tutorial.main import dashboard_tutorial
from reflex_boilerplate.dashboard_tutorial.state import State as dashboard_tutorial_state
from .chatapp_tutorial.main import chatapp_tutorial


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App(
    theme=rx.theme(radius="full", accent_color="grass"),
)
app.add_page(index)
app.add_page(
    dashboard_tutorial, 
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=dashboard_tutorial_state.transform_data,
    route="/dashboard-tutorial")
app.add_page(
    chatapp_tutorial,
    title="Chat App",
    description="A simple app to chat.",
    route="chatapp-tutorial"
)


