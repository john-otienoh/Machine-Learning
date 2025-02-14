import difflib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("./movie.csv")
features = [
    'genres', 'movie_title', 'plot_keywords', 'actor_2_name', 'actor_1_name', 'actor_3_name', 'director_name', 'movie_imdb_link'
]

# Replacing missing values with a string
for feature in features:
    data[feature] = data[feature].fillna('')

# Combining Features
features_combined = data['genres']+' '+data['movie_title']+' '+data['plot_keywords']+' '+data['actor_2_name']+' '+data['actor_1_name']+' '+data['actor_3_name']+' '+data['director_name']+' '+data['movie_imdb_link']

# Converting text to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(features_combined)

# Find Similarity Score
similarity = cosine_similarity(feature_vectors)

# Ask for User Input
movie_name = input("Enter a Movie Name: ")

# Create a list with all the movie names given in thes dataset
movie_title_list = data['movie_title'].to_list()

# Finding Close match for movie name given by user
find_close_match = difflib.get_close_matches(movie_name, movie_title_list)
close_match = find_close_match[0]

# Finding index of movie with title
movie_index = data[data.movie_title == close_match].index.values[0]

# Getting list of similar movies
similarity_score = list(enumerate(similarity[movie_index]))

# Sorting movies based on similarity score
sorted_similar_movies = sorted(similarity_score, key=lambda x:x[1], reverse=True)

# Suggest Top 10 movies to the user
print(f"Movies suggested to you based on {movie_name}")
i = 1
for movie in sorted_similar_movies:
    movie_title = data[data.index == movie[0]]['movie_title'].values[0]
    movie_genre = data[data.index == movie[0]]['genres'].values[0]
    if i <= 10:
        print(f'{i} - {movie_title} under genres like [{movie_genre}]')
        i += 1
