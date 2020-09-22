from flask import Flask, render_template
from flask import request, redirect
import recommender as rec #import all objects from recommender.py
import pickle5 as pickle

app = Flask(__name__) # tells Flask to make THIS script the center of the application


@app.route('/')    # whenever user visits HOSTNAME:PORT/index, this function is triggered: Flask Decorator
@app.route('/index')         # 'index' as name is purely conventiona, could be anything
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
        titles = rec.movieId_to_title(ids)
        movies = dict(zip(titles,ids))
    else:
        movies = dict()
    pkl_filename = "tmp.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(movies, file)
    print(movies)
    return render_template('ratings.html', movies_html=movies.items())


@app.route('/recommendations' , methods = ['POST','GET'])          # Python decorator modifies the function that is defined ON THE NEXT LINE
def recommender():
    with open("tmp.pkl", 'rb') as file:
        user_input_movies = pickle.load(file)
    user_input_ratings = request.form.to_dict()
    user_input = zip(user_input_movies, user_input_ratings.values())
    result = rec.similar_users_recommender(user_input)
    return render_template('recommendations.html', result_html=result)



if __name__ == '__main__':
    # whatever occurs AFTER this line is executed when we run 'python application.py'
    # however, whatever comes AFTER  this line is NOT executed when we IMPORT application.py

    app.run(debug = True)   # this will start an infinite process, i.e. serving our web page.
    #                        # 'debug = True' displays Back-End errors to the browser, which is useful for local development, NOT for production
                            # Also automatically restarts server upon changes to code.
