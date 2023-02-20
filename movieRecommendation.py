# from flask import Flask, jsonify, request
# import pandas as pd
# import numpy as np
# import joblib
# from keras.models import load_model

# model = load_model("movielenssmalllatest_weights.h5")

# movie_df = pd.read_csv("movies.csv")

# def recommend_movies(user_id):
#     movies_watched_by_user = df[df.userId == user_id]
#     movies_not_watched = movie_df[
#         ~movie_df["movieId"].isin(movies_watched_by_user.movieId.values)
#     ]["movieId"]
#     movies_not_watched = list(
#         set(movies_not_watched).intersection(set(movie2movie_encoded.keys()))
#     )
#     movies_not_watched = [[movie2movie_encoded.get(x)] for x in movies_not_watched]
#     user_encoder = user2user_encoded.get(user_id)
#     user_movie_array = np.hstack(
#         ([[user_encoder]] * len(movies_not_watched), movies_not_watched)
#     )
#     ratings = model.predict(user_movie_array).flatten()
#     top_ratings_indices = ratings.argsort()[-10:][::-1]
#     recommended_movie_ids = [
#         movie_encoded2movie.get(movies_not_watched[x][0]) for x in top_ratings_indices
#     ]
#     recommended_movies = movie_df[movie_df["movieId"].isin(recommended_movie_ids)]
#     movie_list = [{"title": row.title, "genres": row.genres} for row in recommended_movies.itertuples()]
#     return jsonify({"movies": movie_list})

