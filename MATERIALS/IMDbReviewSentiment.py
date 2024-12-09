'''
IMDb Reviews Sentiment Analysis
    When run, this script performs a sentiment analysis for movie reviews from IMDb for movies contained in the Bechdel test dataset. It scrapes the review data
    from IMDb and analyzes their sentiments using the VADER sentiment analyzer. The resulting sentiment is added as a column to the dataset. Because of the large
    volume of movie reviews, the script processes movies in batches to efficiently handle the data.

    Ensure that 'bechdel_movies_combined.csv' is in the proper directory with correctly formatted IMDb IDs. Also, this script requires the pandas, requests, 
    BeautifulSoup, nltk, and concurrent.futures libraries.
'''

import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from bs4 import BeautifulSoup
import time

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to fetch IMDb reviews for specific movie based on IMDb ID
def fetch_imdb_reviews(imdbid):
    reviews = []
    url = f"https://www.imdb.com/title/tt{imdbid}/reviews?ref_=tt_ql_3" # url to access the IMDb reviews page for the movie
    
    try:
        response = requests.get(url)  # Make a GET request to fetch the reviews page
        response.raise_for_status() # Error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser') # Parse the response HTML using BeautifulSoup
        
        # Extract review texts from the IMDb reviews page
        review_texts = soup.find_all('div', class_='text show-more__control')
        
        for review in review_texts: # Append text of each review to review list
            reviews.append(review.get_text())
        
        return reviews if reviews else None # return the list of reviews or None if no reviews were found
    
    except requests.exceptions.RequestException as e: # handles any exceptions during http request
        print(f"Error fetching reviews for IMDb ID {imdbid}: {e}")
        return None

# Function to calculate average sentiment score for a list of reviews
def calculate_average_sentiment(reviews):
    if not reviews:
        return None  # if no reviews found

     # Calculate the sentiment score for each review using VADER's polarity_scores method
    sentiment_scores = [analyzer.polarity_scores(review)['compound'] for review in reviews]

    # Return the average sentiment score if the scores exist - return None if they don't
    return sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else None

# Load the dataset containing movies and IMDb IDs
df = pd.read_csv('./data/bechdel_movies_combined.csv')

# Ensure IMDb IDs are properly formatted (should be a string with 7 or more digits)
df['imdbid'] = df['imdbid'].apply(lambda x: str(x).zfill(7))

# Function to process a batch of movies concurrently using multithreading
def process_batch(batch_df, max_workers=10):
    sentiment_scores = [None] * len(batch_df) # list to store sentiment scores for each movie in batch
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor: # fetch reviews and compute sentiment scores
        futures = {executor.submit(fetch_imdb_reviews, row['imdbid']): idx for idx, (index, row) in enumerate(batch_df.iterrows())}

        # proces each future as it is completed
        for future in as_completed(futures):
            idx = futures[future]  # This is now the relative index within the batch
            try:
                reviews = future.result() # gets reviews for movie and calculates average sentiment score
                sentiment_scores[idx] = calculate_average_sentiment(reviews)
            except Exception as e: # handle any exceptions
                print(f"Error processing row {idx}: {e}")
    
    return sentiment_scores # returns list of scores for the batch processed

# Split the dataset into batches and process each batch
def process_movies_in_batches(df, batch_size=100, max_workers=10):
    total_movies = len(df)
    sentiment_scores = []

    for batch_start in range(0, total_movies, batch_size):
        batch_df = df.iloc[batch_start:batch_start + batch_size]
        print(f"Processing batch: {batch_start + 1} to {batch_start + len(batch_df)}")# Process the batch concurrently
        batch_sentiment_scores = process_batch(batch_df, max_workers)
        sentiment_scores.extend(batch_sentiment_scores)
        
        # Optional: Small delay between batches to avoid overwhelming the server
        time.sleep(10)  # Adjust as needed to avoid rate-limiting (optional)
    
    return sentiment_scores

# Fetch sentiment scores in batches
sentiment_scores = process_movies_in_batches(df, batch_size=100, max_workers=10)

# Add the sentiment scores to the dataframe
df['sentiment'] = sentiment_scores

# Save the updated dataframe
df.to_csv('.DATA/bechdel_movies_with_sentiment.csv', index=False)

# Preview the updated dataframe
df.head()
