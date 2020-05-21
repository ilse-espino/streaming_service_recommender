# Analysis on Streaming Services
*Ilse Espino Barros*

*[Data Analytics, Berlin, 22-May-2020]*

## Content
- [Project Description](#project-description)
- [Questions](#questions-and-hypotheses)
- [Dataset](#dataset-and-data-cleaning)
- [Data cleaning](#data-cleaning)
- [Database](#database)
- [Workflow](#workflow)
- [Organization](#organization)
- [Analysis](#Analysis)
- [Links](#links)

## Project Description

Nowadays, we have lots of streaming services available, making it hard to decide on which one to subscribe, since we need to pay for each of them. Netflix is currently the most popular streaming service, having the largest subsricber count, but does that mean that I will like what they are offering? In this project we will look at the content differences on quality (ratings), age content, starting years, runtime minutes, and genres for the following streaming services:
- Netflix
- Amazon Prime Vide
- HBO
- Hulu
- Disney+
Based on their genre differences, a survey was created [survey](https://docs.google.com/forms/d/e/1FAIpQLSfUe-_z6IAdhrEO86mMOE1Yc_qoyl-dPWJnAozNQ1qzyvVA4A/viewform) in order to obtain prefered genres from the user and these, calculate the similarities with each streaming service, allowing us to return the streaming service most similar to the user. The Recommender system can be run on the following notebook: [Streaming Service Recommender v3](https://github.com/ilse-espino/streaming_service_recommender/blob/master/Hulu_and_Disney/Streaming%20Service%20Recommender%20v3.ipynb)

## Questions
- How does each streaming service vary in quality, age content and genres?
- What are the main genres from TV shows available in each streaming service?

## Dataset and Data Cleaning

### Datasets
**Streaming Services TV Shows**

The TV shows data for each streaming service (Netflix, Amazon Prime Video, HBO, Hulu and Disney+) was obtained through webscraping from the website [Reelgood](https://reelgood.com/).
Reelgood is an application which lets you handle all of your subscriptions in one place. It is based on the United States, meaning that this project is based on TV shows content from the United States.

**Genres, average ratings, runtime minutes and release years**

The information for each TV shows was obtained from the [IMDB Datasets](https://www.imdb.com/interfaces/).
These data will not be found on this repository due to its large capacity.

### Data Cleaning

**IMDB Dataset**
- Since the data set from IMDB was to large, containing all available movies and TV shows, a smaller dataset was obtained by filtering the TV related titles (TV series, TV miniseries, etc.).

**Streaming Services Datasets**

- TV shows and IMDB ID's were merged by title and year in order to avoid getting false matches.
- Fuzzy wuzzy library was used in order to get matches for missing titles.
- Null values were removed for each analysis, since they were not directly connected to each other.


## Database

A final data frame was created for each streaming service, including TV show's title, year, age rating, IMDB rating, IMDB ID, start and ending years, runtime minutes and genres.
In order to build the recommender, an individual data frame for TV shows and genres was created for each streaming service. A ratio was calculated for each genre and this values were all combined in a data frame together having each streaming service's genre distribution.


## Workflow

The following workflow was implemented:

**Netflix, Amazon Prime Video and HBO**
1. Gathering data
2. Data cleaning
    - Merge between TV shows and IMDB IDs
    - Verify data types
3. Analysis
5. Creation of Survey
6. Recommender model
7. Link between survey and recommender model
8. Streaming Service Recommender

**Hulu and Disney**
Hulu and Disney were analyzed in added after finishing the Streaming Service Recommender for Netflix, Amazon Prime Video and HBO.
The same process was followed.

## Organization

This repository is divided by Data and Notebook files:
- [Data](https://github.com/ilse-espino/streaming_service_recommender/tree/master/Data): In this folder you may find all exported data from the Netflix, Amazon and HBO Notebooks.
- [Notebooks](https://github.com/ilse-espino/streaming_service_recommender/tree/master/Notebooks): In this folder you may find all notebooks created in order for data acquisition, data cleaning, analysis and recommender model.
- [Hulu and Disney](https://github.com/ilse-espino/streaming_service_recommender/tree/master/Hulu_and_Disney): In this folder you may find all notebooks created in order for data acquistion, data cleaning, analysis and recommender model including the 5 streaming services, as well as a folder titled [Data Hulu Disney](https://github.com/ilse-espino/streaming_service_recommender/tree/master/Hulu_and_Disney/Data_Hulu_Disney) for all exported data for these notebooks.

## Analysis

Interesting findings were made for IMDB ratings, age ratings and genres.

### IMDB Ratings

**HBO**

75% of HBO's TV shows have a rating of 7/10 or greater. HBO has always favored quality over quantity, which can also be seen by their 200 TV shows available, different from Netflix, Amazon and Hulu. Also, it has always been subscription-based, being the most expensive onne from the rest, leading to suggest that their audience will expect greater quality content than the rest.

**Netflix, Amazon and Hulu**

These three streaming services have 50% of their TV shows with a rating of 7/10 or greater. These have the greatest TV shows' catalog, ranging from 1,500 to 3,000, making it hard to have all TV shows with a high rating.

**Disney+**

Surprisingly, Disney+ has only 25% of their TV shows with rating of 7/10 or greater. Being a great franchise it would be expected for them to have better quality, but in this project we are only focusing on TV shows, not movies, for which they are better known for. Similar to HBO, Disney+ has only original content, only having 180 TV shows available, but according to my research, Disney’s TV shows have lower ratings due to the fact that they lack originality, since their TV shows have been really similar to each other lately.

### Age Content

**HBO**

HBO has a target audience of older people, ranging from 30-50 years. This matches their content available having almost 80% of their available shows for 18 years or older, and having very few TV shows available for all ages, such as Sesame Street.

**Hulu**

Hulu's TV shows are distributed for all age groups (adults, teenagers and children), but has more available TV shows for teenagers. Their target audience is a most younger public, ranging from 20-30 years old.

**Netflix**

Netflix is really equally balanced between all groups. Their target audience ranges from 18 to 50 years, sort of a combination of HBO and Hulu. This may also be a reason why it is the most popular streaming service.

**Amazon Prime Video**

Amazon Prime Video is really similar to Netflix and Hulu but has more content available for Children, or all ages.

**Disney+**

Disney+ has around 80% of their TV shows available for all ages, having none for 18 years or older. Their target audiences are families or households with at least one child.

### Genres

All streaming services shared 26 genres in total, all of them having Comedy and Drama listed as their top genres, except for Disney, which had Drama in a lower place. Out of all, Amazon and Netflix had a really similar distribution of genres. In the following list wee will order the genres which stand out from each streaming service:

- Netflix: Horror, Thriller and Romance
- Amazon Prime Video: Documentaries and Fantasy
- HBO: Mystery, Sports and History
- HULU: Game-Shows and Reality-TV
- Disney+: Adventure, Family, Music/Musical, and Sci-Fi


## Links

- [IMDB Data](https://www.imdb.com/interfaces/)
- [Reelgood](https://reelgood.com/)
- [Slides](https://drive.google.com/open?id=1bcwL9WdrmTKaqlvD5sxGIXZtGOFIpJTU0jGaEhnG5Nw)
