import pandas as pd
import numpy as np
import re
from fuzzywuzzy import fuzz
from scipy.spatial.distance import pdist, squareform

def get_recommender_df(survey_df, df_all_shows):
    
    while True:
        
        name = input("Please enter your name:")
        
        try:

            if name in survey_df["Name"].values:
                break;
            
            else:
                print("That user name does not match. Please try again.")
                
        except ValueError:
            print("That user name does not match. Please try again.")

    user_df = survey_df.loc[np.where(survey_df["Name"] == name)]
    
    user_df["Timestamp"] = pd.to_datetime(user_df["Timestamp"])
    
    user_df = user_df.iloc[np.where(user_df["Timestamp"] == user_df["Timestamp"].max())]
    
    user_df = user_df.drop(columns=["Timestamp", "Name"])
   
    genre_columns = ['Crime', 'Drama', 'Thriller', 'Fantasy', 'Horror', 'Mystery', 'Comedy', 'Sci-Fi', 'Biography',
                 'Action', 'Adventure', 'Romance', 'History', 'Documentary', 'Animation', 'War', 'Sport',
                 'Family', 'Western', 'Short', 'Reality-TV', 'Musical', 'Music', 'Game-Show', 'Talk-Show', 'News']
        
    all_shows_lst = [show for show in df_all_shows["show"]]
    
    titles = []
        
    # we will select just the last element using the tail pandas method
    for show in user_df.values[0]:
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
    
    return user_recommender, name


def get_streaming_recommendation(genres_recommender, user_survey, name):
    
    recommendations = []
    
    user_recommender = genres_recommender.append(user_survey)
           
    distances_df = pd.DataFrame((squareform(pdist(user_recommender, 'euclidean'))), 
                                 index=user_recommender.index, columns=user_recommender.index)
    
    similar_streamings = list(distances_df['User'].sort_values()[1:].index)
    distances = list(distances_df['User'].sort_values()[1:].values)
    
    # we will increase the range in order to get the similarities for all 5 streaming services
    for i in range(5):
        recommendations.append(similar_streamings[i])
       
    # we will show the percentage of similarity, whcih is 1 minus the distance multiplied by a 100
    print("\n")
    print(f"Matches for {name}")
    print("--------------------------")
    print("Your closest match is " + recommendations[0] + f" with {int(1/(1+distances[0])*100)}% genre similarity.")
    print("\n")
    print("Your next matches are:")
    print("2. " + recommendations[1] + f" with {int(1/(1+distances[1])*100)}% genre similarity.")
    print("3. " + recommendations[2] + f" with {int(1/(1+distances[2])*100)}% genre similarity.")
    print("4. " + recommendations[3] + f" with {int(1/(1+distances[3])*100)}% genre similarity.")
    print("5. " + recommendations[4] + f" with {int(1/(1+distances[4])*100)}% genre similarity.")
    
    return ("")
