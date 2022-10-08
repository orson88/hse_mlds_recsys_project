# hse_mlds_reccsys_project
A repo for an annual group project from machine learning and highload system course in Higher School of Economics.

### Timeline:

|date   |task   |
|-------|-------|
|**30.09.2022**|work environment setup: notion, trello, github|
|**07.10.2022**|to choose a dataset on kaggle|

### Concept
We plan to develop a recommendation system for music as a web app. 
Te project consists 3 steps:
1. Exploratory data analysis of the dataset, development of 
   simple web app for metrics calculation and data visualization. 
2. Development of different classic ML models, choice of the best one 
   and deployment it into the app. As a result, we plan to build 
   the functionality of getting top N tracks for given user.
3. Development of DL model and deployment it into the app to increase 
   the quality of recommendations
   
### Datasets
`pip install kaggle`
1. Spotify dataset

`kaggle datasets download -d vatsalmavani/spotify-dataset -p ./datasets/spotify`

`unzip datasets/spotify/spotify-dataset.zip -d datasets/spotify && rm datasets/spotify/spotify-dataset.zip`