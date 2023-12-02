# Movie Recommender
#### Video Demo:  url
#### Description:

This is my final project for CS50’s Introduction to Computer Science.

My project is called "Movie Recommender". It is a movie recommendation system that uses a dataset from kaggle called "the-movies-dataset". Python's pandas library was used to manipulate the data quickly and efficiently. I used the OMDB API to get the movie's posters to display after being recommending one.

project.py in the `projects` directory is where all the code is stored. movies_metadata.csv is the data set. In the `assets` directory, the icon is stored.

reflex was used to create the frontend. Reflex is a pyton module that allows for the creation of web applications with only python.

There is a dropdown menu that allows the selection of the genre of the movie. There is a switch that enables recommendation of adult content. When the the adult-mode is on, it with recommend both adult and non-adult movies. The slider is used to adjust the maximum runtime of the recommended movie. When pressing the recommend button, a 7 by 1 table is generated that contains the information of the movie: 

* Title
* Poster
* Plot
* Rating
* Actors
* Runtime
* 

There are multiple error handling processes within the program as shown in the video. There is also a function that allows for the use of light mode and dark mode.


#### Setup

This program is locally runnable via the command line, using localhost and port 3000. This has been tested on python 3.10.12 in ubuntu but should work with most other versions.

```
pip install -r requirements.txt
reflext init
reflex run
```

#### Sources

https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

https://www.omdbapi.com/

https://reflex.dev/
