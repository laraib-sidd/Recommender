import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def anime_recommendation(anime_name):
    # try:

    print(f"Anime name in the script is: {anime_name}")
    print("--------------------------------------------")
    loc = "scripts/Anime/filtered_data.csv"
    df = pd.read_csv(loc)

    # except:
    #     print('REACHED EXCEPT STATEMENT IN ANIME FILE, UNABLE TO READ THE DATA')
    #     print('---------------------------------------------------------------------')

    anime_features = df.loc[:, "Movie":].copy()

    cosine_sim = cosine_similarity(anime_features.values, anime_features.values)

    anime_index = pd.Series(df.index, index=df.name).drop_duplicates()
    idx = anime_index[anime_name]

    # Get the pairwise simalirity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the simalirity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar anime
    sim_scores = sim_scores[0:11]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar anime
    result = df[["name", "genre", "community_rating"]].iloc[anime_indices].drop(idx)

    return result


if __name__ == "__main__":
    print('Try on the recommendation system with "Steins;Gate')
    pred = anime_recommendation("Steins;Gate")
    print(pred)
