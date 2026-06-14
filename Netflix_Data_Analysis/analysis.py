import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("netflix_data.csv")
"""
step 1 : creating a structure 
step 2 : validating the information
step 3 : finding the missing values 
step 4 : filling the missing values
step 5 : movies vs tv show analysis
step 6 :  Which countries contribute the most content on Netflix?
step 7 : most popular genere 

"""
print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
#step3 - finding the missing value 
print(df.isnull().sum())
# step 4 -> found 38 -> directors , 11 -> cast , 40 -> country values are missing 
# start with director -> value to unknown
df["director"] = df["director"].fillna("unkown")
# country -> not specfified
df["country"] = df["country"].fillna("Not Specified")
# cast -> not avaliable 
df["cast"] = df["cast"].fillna("Not Available")
#done dealing with missing data 
#step 5 -Movies vs TV Shows Analysis
content_count = df["type"].value_counts()
print(content_count)
#plot a bar graph for the contents 
plt.bar(content_count.index,content_count.values)
plt.xlabel("Count")
plt.title("Movies V/S T V shows on Netflix") 
plt.savefig("images/Movies_VS_TV_shows_on_Netflix_bar.png")
plt.show()
#pie chart 
plt.pie(
    content_count.values,
    labels= content_count.index,
    autopct = "%1.1f%%"
)
plt.savefig("images/Movies_VS_TV_shows_on_Netflix_pie.png")
plt.show()

# step 6: Which countries contribute the most content on Netflix?
country_df = df.copy()
country_df["country"]= country_df["country"].str.split(",")
country_df = country_df.explode("country")
top_countries = (
    country_df["country"].value_counts().head()
)
print(top_countries)

#horizontal bar chart 
plt.figure(figsize=(10,6))
plt.barh(
    top_countries.index,
    top_countries.values
)
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.savefig("images/Top_10_Countries_Producing_Netflix_Content.png")
plt.show()

#step 7 : most popular genere 
genre_df = df.copy()
genre_df["listed_in"] = genre_df["listed_in"].str.split(", ")
genre_df = genre_df.explode("listed_in")
top_genres = (
    genre_df["listed_in"]
    .value_counts()
    .head(10)
)
print(top_genres)

plt.figure(figsize=(10,6))

plt.barh(
    top_genres.index,
    top_genres.values
)

plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.title("Top 10 Most Popular Genres on Netflix")
plt.savefig("images/Top_10_Most_Popular_Genres_on_Netflix.png")

plt.show()

#ratings 
print(df["rating"].head())
rating_count = df["rating"].value_counts()
top_ratings = df["rating"].value_counts().head(20)
plt.figure(figsize=(10,6))

plt.bar(
    top_ratings.index,
    top_ratings.values
)

plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.title("Netflix Content Ratings Distribution")
plt.xticks(rotation=45)
plt.savefig("images/ratings.png")
plt.show()
print(rating_count)

#movie duration 
movies_df = df.loc[df["type"] == "Movie"]
movies_df["duration"] = movies_df["duration"].str.replace(" min", "")
movies_df["duration"] = movies_df["duration"].astype(int)
movies_df["duration"].mean()
movies_df["duration"].max()
movies_df["duration"].min()
movies_df["duration"].describe()
plt.figure(figsize=(10,6))
plt.hist(
    movies_df["duration"],
    bins=20
)
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movie Durations on Netflix")
plt.savefig("Distribution_of_Movie_Durations_on_Netflix.png")
plt.show()