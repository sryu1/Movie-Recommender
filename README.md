# Movie Recommender

#### Video Demo: <https://youtu.be/wf1IGRGqVi0>

#### Description

This is my final project for CS50’s Introduction to Computer Science.

My project is called "Movie Recommender". It is a movie recommendation system that uses a dataset from kaggle called "the-movies-dataset". Python's pandas library was used to manipulate the data quickly and efficiently. I used the OMDB API to get the movie's posters to display after being recommending one.

project.py in the `projects` directory is where all the code is stored. movies_metadata.csv is the data set. In the `assets` directory, the icon is stored.

Reflex was used to create the frontend. Reflex is a pyton module that allows for the creation of web applications with only python.

There is a dropdown menu that allows the selection of the genre of the movie. There is a switch that enables recommendation of adult content. When the the adult-mode is on, it with recommend both adult and non-adult movies. The slider is used to adjust the maximum runtime of the recommended movie. When pressing the recommend button, a 7 by 1 table is generated that contains the information of the movie:

* Title
* Poster
* Plot
* Rating
* Actors
* Runtime
* Awards

There are multiple error handling processes within the program as shown in the video. There is also a function that allows for the use of light mode and dark mode.

using requests' `requests.get()` function with the title, the OMDB movies api returned a json format, with the movie it, as an example:

```json
{"Title":"It","Year":"2017","Rated":"R","Released":"08 Sep 2017","Runtime":"135 min","Genre":"Horror","Director":"Andy Muschietti","Writer":"Chase Palmer, Cary Joji Fukunaga, Gary Dauberman","Actors":"Bill Skarsgård, Jaeden Martell, Finn Wolfhard","Plot":"In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.","Language":"English, Hebrew","Country":"United States, Canada","Awards":"10 wins & 46 nominations","Poster":"https://m.media-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjYi00ZjhhLWE1ODEtMWMzMWMzNDA0NmQ4XkEyXkFqcGdeQXVyNzYzODM3Mzg@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.3/10"},{"Source":"Rotten Tomatoes","Value":"86%"},{"Source":"Metacritic","Value":"69/100"}],"Metascore":"69","imdbRating":"7.3","imdbVotes":"588,623","imdbID":"tt1396484","Type":"movie","DVD":"19 Dec 2017","BoxOffice":"$328,874,981","Production":"N/A","Website":"N/A","Response":"True"}
```

From this, indexing was used to find the information needed to display onto the web program. Reflex's `rx.image` was used to display the image in the browser. Using python's try/except functions, when the api returned an error for some reason, the program tries re-recommending another movie.

In terms of styling, the reflex supported the use of css styling as well, thus, it was used to display the UI correctly.

#### Setup

This program is locally runnable via the command line, using localhost and port 3000. This has been tested on python 3.10.12 in ubuntu but should work with most other versions.

```
pip install -r requirements.txt
reflext init
reflex run
```

#### Sources

<https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset>

<https://www.omdbapi.com/>

<https://reflex.dev/>
