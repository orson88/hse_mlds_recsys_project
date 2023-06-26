# hse_mlds_reccsys_project
A repo for an annual group project from machine learning and highload system course in Higher School of Economics.

### Run Jupyter Lab server with standardized environment:
#### Build the image:
`docker build -t project_jupyterlab .`
#### Run a container:
`docker run --rm -v $(PWD)/app/:/hse_mlds_recsys_project/app -v $(PWD)/experiments/:/hse_mlds_recsys_project/experiments -v $(PWD)/datasets/:/hse_mlds_recsys_project/datasets -p 8877:8888 --name jupyterlab_container project_jupyterlab`
##### Note:
You can change your local port: `-p <yourLocalPort>:8888` 


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
1. Users & Playlists from Spotify

`https://www.kaggle.com/datasets/andrewmvd/spotify-playlists`

2. Songs features

`wget --no-verbose https://www.dropbox.com/s/sr4ejcgeedlt79m/tracks_feats.csv`

### RecSys App

each service should be launched from separate terminal instnces
- run FastApi backend service

`` python -m uvicorn web_app.ourapi:app --reload --port 8054``

- run streamlit frontend service

`` streamlit run web_app/main.py --server.port 8090``

### Cluster usage
switch to branch arspoz to see the further guide
##
