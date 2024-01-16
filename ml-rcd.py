import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'User': ['User1', 'User1', 'User2', 'User2', 'User3', 'User3'],
    'Movie': ['Movie1', 'Movie2', 'Movie2', 'Movie3', 'Movie1', 'Movie3'],
    'Rating': [5, 4, 3, 2, 5, 1]
}

df = pd.DataFrame(data)
print(df)

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

user_item_matrix = train_data.pivot_table(index='User', columns='Movie', values='Rating')
user_item_matrix = user_item_matrix.fillna(0)  # Fill NaN values with 0

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def get_movie_recommendations(user):
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]  # Exclude the user itself
    user_movies = user_item_matrix.loc[user]

    recommendations = []

    for sim_user in similar_users:
        sim_user_movies = user_item_matrix.loc[sim_user]
        new_movies = sim_user_movies[sim_user_movies > 0].index.difference(user_movies[user_movies == 0].index)
        recommendations.extend(new_movies)

    return recommendations


# Example: Get movie recommendations for 'User1'
# user1_recommendations = get_movie_recommendations('User1')
# print("Recommendations for User1:", user1_recommendations)