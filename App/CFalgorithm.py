import pandas as pd

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
# ratings.head()
user_ratings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
user_ratings = user_ratings.dropna(thresh=0,axis=1).fillna(0)
item_similarity_df = user_ratings.corr(method='pearson')
# item_similarity_df.head(50)

def get_similar_movies(movie_name,user_rating):
    similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score
# action_lover = [("(500) Days of Summer (2009)",5),
#                 ("10 Cloverfield Lane (2016)",1),
#                 ("10,000 BC (2008)",1)]
# similar_movies = pd.DataFrame()
# print(similar_movies)
# for movie,rating in action_lover:
#     similar_movies = similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)
# # similar_movies.head()。
# print(similar_movies.sum().sort_values(ascending=False))