import pandas as pd
import numpy as np
import re
from fuzzywuzzy import fuzz
from scipy.spatial.distance import pdist, squareform


def get_recommender_df(survey_df, df_all_shows):
    
    genre_columns = ['Crime', 'Drama', 'Thriller', 'Fantasy', 'Horror', 'Mystery', 'Comedy', 'Sci-Fi', 'Biography',
                 'Action', 'Adventure', 'Romance', 'History', 'Documentary', 'Animation', 'War', 'Sport',
                 'Family', 'Western', 'Short', 'Reality-TV', 'Musical', 'Music', 'Game-Show', 'Talk-Show', 'News']
    
    survey_df = survey_df.drop(columns="Timestamp")
    
    all_shows_lst = [show for show in df_all_shows["show"]]
    
    titles = []
        
    # we will select just the last element using the tail pandas method
    for show in survey_df.tail(1).values[0]:
        # remove the year and description
        title_pattern = r"(.*)\s\(\d{4}\).*$"
        title = re.findall(title_pattern, show)
        titles.append(title[0])

    matches = []

    for title in titles:
        for show in all_shows_lst:
            ratio = fuzz.ratio(title.lower(), show.lower())
            if ratio == 100:
                matches.append(show)
                matches = list(set(matches))
                              
    user_df = df_all_shows[df_all_shows["show"].isin(matches)].reset_index(drop=True)
    
    user_genre_ratio = (pd.DataFrame(user_df[genre_columns].sum()
                                    .sort_values(ascending=False))
                       .reset_index()
                       .rename(columns={"index":"genre", 0:"frequency"}))

    user_genre_ratio["ratio"] = round((user_genre_ratio["frequency"] / 30), 4)

    user_genre_ratio["user"] = "User"

    user_recommender = user_genre_ratio.pivot_table(index="user",
                                          columns="genre",
                                          values="ratio")
    
    return user_recommender


def get_streaming_recommendation(genres_recommender, user_survey, no=1):
    
    recommendations = []
    
    user_recommender = genres_recommender.append(user_survey)
        
    distances = squareform(pdist(user_recommender, 'euclidean'))
    
    distances_df = pd.DataFrame((squareform(pdist(user_recommender, 'euclidean'))), 
                         index=user_recommender.index, columns=user_recommender.index)
    
    similarities = list(distances_df['User'].sort_values()[1:].index)
    
    for i in range(no):
        recommendations.append(similarities[i])
    
    for j in range(len(recommendations)):
        print(f"{j+1}. " + recommendations[j])
    
    # We need to add a return value beacuse if not the streaming_recommendations returns None at the end, we will return
    # a blank string
    return ("")


# genres_recommender, survey_df, df_all_shows

def streaming_recommendations(genres_recommender, survey_df, df_all_shows):
    
    while True:
        no_recommendations = input("How many recommendations would you like from 1 to 3?")
        try:
            no_recommendations = int(no_recommendations)
            if no_recommendations < 4:
                break;
            else:
                print ("The number entered is greater than 3. Please enter a number from 1 to 3.")
        except ValueError:
            print ("That is not a valid entry.")
   
    user_survey = get_recommender_df(survey_df, df_all_shows)
            
    print("\n")
    print("Your recommendations in order from most similar to less are the following:")
    print(get_streaming_recommendation(genres_recommender, user_survey, no=no_recommendations))
