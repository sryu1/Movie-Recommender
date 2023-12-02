from rxconfig import config
import reflex as rx
import pandas as pd
import random
import requests


movies = pd.read_csv("movies_metadata.csv", low_memory=False)
filename = f"{config.app_name}/{config.app_name}.py"
API_KEY = "a26b7da7"


class State(rx.State):
    selected_genre: str = "Select Genre"
    checked: bool = False
    is_checked: bool = False
    runtime: int = 120
    movie = "N/A"
    plot = "N/A"
    movie_runtime = "N/A"
    actors = "N/A"
    rating = "N/A"
    awards = "N/A"
    show_recommendation: bool = False
    poster = "Poster not available"

    def change_check(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.is_checked = True
        else:
            self.is_checked = False

    def recommend(self):
        genre = self.selected_genre
        adult = self.is_checked
        runtime = self.runtime
        adult_find = movies[movies["adult"] == str(adult)]
        if adult:
            genre_find = movies.loc[movies["genres"].str.contains(genre)]
            runtime_find = genre_find.loc[movies["runtime"] < runtime]
            aruntime_find = runtime_find.loc[movies["runtime"] != 0]
            movie_find = (aruntime_find["title"]).values.tolist()
        else:
            genre_find = adult_find.loc[movies["genres"].str.contains(genre)]
            runtime_find = genre_find.loc[movies["runtime"] < runtime]
            aruntime_find = runtime_find.loc[movies["runtime"] != 0]
            movie_find = (aruntime_find["title"]).values.tolist()
        try:
            rand = random.randint(0, len(movie_find))
            self.movie = movie_find[rand]
            self.poster = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Poster"]
            self.actors = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Actors"]
            self.rating = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Ratings"][0]["Value"]
            self.plot = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Plot"]
            self.plot = " ".join(
                [
                    self.plot.split()[i] + "<br><br>"
                    if (i + 1) % 15 == 0
                    else self.plot.split()[i]
                    for i in range(len(self.plot.split()))
                ]
            )
            self.awards = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Awards"]
            self.movie_runtime = aruntime_find["runtime"].values.tolist()[rand]
            self.show_recommendation = True
        except IndexError:
            return rx.window_alert("Please select a genre")
        except KeyError:
            rand = random.randint(0, len(movie_find))
            self.movie = movie_find[rand]
            self.poster = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Poster"]
            self.actors = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Actors"]
            self.rating = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Ratings"][0]["Value"]
            self.plot = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Plot"]
            self.plot = " ".join(
                [
                    self.plot.split()[i] + "<br><br>"
                    if (i + 1) % 15 == 0
                    else self.plot.split()[i]
                    for i in range(len(self.plot.split()))
                ]
            )
            self.awards = requests.get(
                "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + self.movie
            ).json()["Awards"]
            self.movie_runtime = aruntime_find["runtime"].values.tolist()[rand]
            self.show_recommendation = True


@rx.page(route="/", title="Movie Recommender")
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
            rx.cond(
                State.show_recommendation,
                rx.table_container(
                    rx.table(
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text("Title", font_size="10px", align="center"),
                                    rx.text(State.movie, align="center"),
                                    align="center",
                                ),
                            ),
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text("Poster", font_size="10px", align="center"),
                                    rx.image(
                                        src=State.poster,
                                        alt="Movie Poster",
                                        align="center",
                                    ),
                                    align="center",
                                ),
                            )
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text("Plot", font_size="10px", align="center"),
                                    rx.html(State.plot, align="center"),
                                    align="center",
                                ),
                            )
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text(
                                        "IMDB Rating", font_size="10px", align="center"
                                    ),
                                    rx.text(State.rating, align="center"),
                                    align="center",
                                ),
                            )
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text("Actors", font_size="10px", align="center"),
                                    rx.text(State.actors, align="center"),
                                    align="center",
                                ),
                            )
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text(
                                        "Runtime", font_size="10px", align="center"
                                    ),
                                    rx.text(
                                        f"{State.movie_runtime} Minutes", align="center"
                                    ),
                                    align="center",
                                ),
                            )
                        ),
                        rx.tr(
                            rx.td(
                                rx.box(
                                    rx.text("Awards", font_size="10px", align="center"),
                                    rx.text(State.awards, align="center"),
                                    align="center",
                                ),
                            )
                        ),
                        headers=[rx.text("Movie", align="center")],
                    ),
                    align="center",
                    center_content=True,
                ),
            ),
            font_size="2em",
        ),
    )


app = rx.App()
app.add_page(index)
app.compile()
