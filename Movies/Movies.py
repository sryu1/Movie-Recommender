"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import pandas as pd
import random


movies = pd.read_csv("movies_metadata.csv", low_memory=False)

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    selected_genre: str = "Select Genre"

    checked: bool = False
    is_checked: bool = False

    def change_check(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.is_checked = True
        else:
            self.is_checked = False

    runtime: int = 120

    def recommend(self):
        genre = self.selected_genre
        adult = self.is_checked
        runtime = self.runtime
        adult_find = movies[movies["adult"] == str(adult)]
        if adult:
            genre_find = movies[movies["genres"].str.contains(genre)]
            runtime_find = genre_find[movies["runtime"] < runtime]
            aruntime_find = runtime_find[movies["runtime"] != 0]
            movie_find = (aruntime_find["title"]).values.tolist()
        else:
            genre_find = adult_find[movies["genres"].str.contains(genre)]
            runtime_find = genre_find[movies["runtime"] < runtime]
            aruntime_find = runtime_find[movies["runtime"] != 0]
            movie_find = (aruntime_find["title"]).values.tolist()
        try:
            print(movie_find[random.randint(0, len(movie_find))])
        except IndexError:
            return rx.window_alert("Please select a genre")


genre = State.selected_genre
adult = State.is_checked
runtime = State.runtime


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Movie Recommender", font_size="2em"),
            rx.menu(
                rx.menu_button(
                    State.selected_genre,
                    style={"fontSize": "25px"},
                    border="0.1em solid",
                    border_radius="0.5em",
                    padding="0.05em",
                ),
                rx.menu_list(
                    rx.menu_item(
                        "Animation",
                        on_click=lambda: State.set_selected_genre("Animation"),
                    ),
                    rx.menu_item(
                        "Mystery", on_click=lambda: State.set_selected_genre("Mystery")
                    ),
                    rx.menu_item(
                        "Romance", on_click=lambda: State.set_selected_genre("Romance")
                    ),
                    rx.menu_item(
                        "Family", on_click=lambda: State.set_selected_genre("Family")
                    ),
                    rx.menu_item(
                        "Comedy", on_click=lambda: State.set_selected_genre("Comedy")
                    ),
                    rx.menu_item(
                        "Fantasy", on_click=lambda: State.set_selected_genre("Fantasy")
                    ),
                    rx.menu_item(
                        "Adventure",
                        on_click=lambda: State.set_selected_genre("Adventure"),
                    ),
                    rx.menu_item(
                        "Crime", on_click=lambda: State.set_selected_genre("Crime")
                    ),
                    rx.menu_item(
                        "Horror", on_click=lambda: State.set_selected_genre("Horror")
                    ),
                    rx.menu_item(
                        "Action", on_click=lambda: State.set_selected_genre("Action")
                    ),
                    style={"fontSize": "15px"},
                ),
            ),
            rx.text("Adult Content"),
            rx.switch(
                is_checked=State.checked,
                on_change=State.change_check,
            ),
            rx.heading(f"Maximum {State.runtime} Minutes"),
            rx.slider(
                on_change_end=State.set_runtime,
                width="25%",
                min_=30,
                max_=180,
            ),
            rx.button(
                "Recommend",
                on_click=lambda: State.recommend,
                font_size="1em",
                padding="0.5em",
                border_radius="0.2em",
            ),
            font_size="2em",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
