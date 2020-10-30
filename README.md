# POPCORN

A **Movie Recommender** built with a web interface. This project entails a web-based movie recommender engine using two different recommendation models: **NMF** (Negative Matrix Factorization algorithm) and an **User-based Cosimilarity Matrix** recommender algorithm that takes the top 10 most similar users and creates a new movie vector from their ratings average to recommend movies that would most likely be appreciated by the user giving the rating inputs. This is a collaborative project, and it is still in development.
<img src="https://github.com/brauliotegui/POPCORN/blob/master/demo1.gif">
<img src="https://github.com/brauliotegui/POPCORN/blob/master/demo2.gif">

## Link: 
http://novi.pythonanywhere.com/

_Portuguese-BR version of the web-app, deployed_

## Models:
  **1. NMF:** Negative matrix factorization
  
  **2. Cosim:** User-based cosimilarity matrix model. This option creates a new user with ratings of the given movies (all consider 5) and recommend movies from similar user ratings
  

## Tech used:
 - Python
 - Flask
 - HTML
 - CSS
 - PostgreSQL
 - sqlalchemy
 - Scikit-learn
