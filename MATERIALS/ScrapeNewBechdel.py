'''
IMDb Bechdel Test Movies Scraper and Dataset Merger
    The purpose of this script is to scrape newer data from the Bechdel test website, checking for movies that were added after the most recent date in a preexisting dataset, 
    efficiently combining the new and old datasets into a more robust dataset. It can scrape up to 3 pages of new movies, checks the API for detailed information, then updating
    the new dataset after removing any multiples.

    To run this code, you need to have 'bechdel_movies_2023_FEB.csv' in the proper directory, as well as the pandas, requests, BeautifulSoup, re, and timeit libraries.
'''

# Import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from timeit import default_timer as timer

# Load the existing dataset
old_movies_df = pd.read_csv('./DATA/bechdel_movies_2023_FEB.csv')

# Convert the 'date' column to datetime format in the existing dataset
old_movies_df['date'] = pd.to_datetime(old_movies_df['date'])

# Find the latest date in the existing dataset to filter new movies
latest_old_date = old_movies_df['date'].max()
print(f"The latest date in the old dataset: {latest_old_date}")

# Status code check to make sure the Bechdel test website is accessible
response = requests.get('https://bechdeltest.com/?page=0', timeout=10)
if response.status_code == 200:
    print('Hi! How can I help you? :)')
else:
    print(f'Sorry but {response.status_code} occurred')

# List to store IMDb IDs of newly added movies
new_movie_imdbid = []

# Loop over pages of the Bechdel test website (update to scrape 3 pages as required)
for i in range(3):
    url = f'https://bechdeltest.com/sort/added?page={i}'
    response = requests.get(url)
    html_content = response.text
    
    # Extract IMDb IDs from the HTML page content using regex
    regex_pattern = r'title/tt(\d+)/'
    matches = re.findall(regex_pattern, html_content)

    # Add each IMDb ID to the list
    for imdbid in matches:
        new_movie_imdbid.append(imdbid)
        if imdbid == '2371399':  # If specific IMDb ID is reached, stop the loop
            break

    if imdbid == '2371399':
        break

print(new_movie_imdbid) # IMDb Movie IDs scraped

# Check the number of newly added movies
print(f"Number of newly added movies in the list: {len(new_movie_imdbid)}")

# Initialize list to store movie information about the new movies
new_movies_info = []

# Scrape data for each IMDb ID
start = timer() # measure scraping time
for count, imdbid in enumerate(new_movie_imdbid, start=1): # loop over each ID to get information
    url = f'http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid={imdbid}'
    
    # Send API request to fetch movie data
    try:
        response = requests.get(url)
        response.raise_for_status()
        movie_info = response.json()
        
        # Add movie only if it was uploaded after the latest date in the old dataset
        movie_date = pd.to_datetime(movie_info.get('date'))
        if movie_info.get('title') and movie_date > latest_old_date:
            new_movies_info.append(movie_info)
        
    except requests.exceptions.HTTPError as error: # print error message if API request fails
        print(f"HTTP Error ({error}): {url}")
        continue 
    
    print(f"Scraped movie {count}/{len(new_movie_imdbid)}: {imdbid}") # Print progress after each movie is processed

# Convert list of new movies to DataFrame
new_movies_df = pd.DataFrame(new_movies_info)

# Save the scraped data into CSV
new_movies_df.to_csv('./DATA/new_movies.csv', index=False)

# Reindex columns to match old dataset before merging
new_movies_df = new_movies_df.reindex(columns=['title', 'year', 'rating', 'dubious', 'imdbid', 'id', 'submitterid', 'date', 'visible'])

# Merge the new dataset with the old one
combined_df = pd.concat([old_movies_df, new_movies_df], ignore_index=True)

# Remove duplicate entries
combined_df.drop_duplicates(inplace=True)

# Save the final combined dataset as CSV
combined_df.to_csv('./DATA/bechdel_movies_combined.csv', index=False)

# Print time taken for entire process
print(f'It took {timer() - start} seconds to scrape all the information and combine the datasets.')
