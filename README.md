# POPCORN

A **Movie Recommender** built with a web interface. This project entails a web-based movie recommender engine using two different recommendation models: NMF, Negative Matrix Factorization algorithm, and an user-based cosimilarity matrix recommender algorithm that takes the top 10 most similar users and creates a new movie vector from their ratings average to recommend movies that would most likely be appreciated by that new similar user. This is a collaborative project that still in development.

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
