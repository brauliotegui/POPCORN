from flask import Flask, render_template, request
from recommender import calculate_best_movies
from recommender import similar_users_recommender
from recommender import movieId_to_title

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
# make this file the center of the app
# We launch this file from the terminal to start the app

@app.route('/')
@app.route('/index')  # whatever the function below this, route it to the path
def index():
    movies=[]
    return render_template('index.html')


@app.route('/ratings', methods = ['POST','GET'])
def ratings():
    user_input = dict(request.form)              # copied from github to make it worl
    print(user_input)
    if 'movielist' in user_input.keys():
        movielist = user_input['movielist']
        ids = list(map(int, movielist.split(',')))
        titles = movieId_to_title(ids)
        movies = dict(zip(titles,ids))
    else:
        movies = dict()
    print(movies)
    return render_template('ratings.html', movies_html=movies.items())



@app.route('/recommender')
def recommender():
    user_input = dict(request.args)
    user_input_movies = list(user_input.values())[:-1:2]
    user_input_ratings = list(user_input.values())[1:-1:2]
    user_input_model = list(user_input.values())[-1]
    user_input = zip(user_input_movies, user_input_ratings)
    if user_input_model == 'NMF':
        result = calculate_best_movies(10, user_input_movies, user_input_ratings)
    else:
        result = similar_users_recommender(10, user_input_movies, user_input_ratings)
    return render_template('recommender.html', result=result, user_input=user_input)

if __name__ == '__main__':
    # whatever occurs AFTER this line is executed when we run 'python application.py'
    # however, whatever comes AFTER  this line is NOT executed when we IMPORT application.py

    app.run(debug = True)   # this will start an infinite process, i.e. serving our web page.
    #                        # 'debug = True' displays Back-End errors to the browser, which is useful for local development, NOT for production
                            # Also automatically restarts server upon changes to code.
