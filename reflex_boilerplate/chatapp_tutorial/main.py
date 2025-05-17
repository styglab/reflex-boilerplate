import reflex as rx

from . import style
from .state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em",
        width="100%",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", 
                  on_click=State.answer,
                  style=style.button_style,
        ),
    )

def chatapp_tutorial() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
        )

