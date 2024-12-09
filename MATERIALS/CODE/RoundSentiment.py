'''
Round Sentiment Scores in Bechdel Dataset
  Running this script will result in loading a dataset of movies including sentiment scores from IMDb reviews. For clean presentation, each sentiment score is rounded to 2
  decimal places. Additionally, the updated dataset is saved to a new CSV file, 'bechdel_movies_with_sentiment.csv'. You can also choose to print the first few rows of the new
  dataset to confirm that the proper changes were made.

  This script only requires the pandas library.
'''

import pandas as pd

# Load the dataset that contains the sentiment scores and movie data
df = pd.read_csv('./DATA/bechdel_movies_with_sentiment.csv')

# Round the sentiment column to two decimal places
df['sentiment'] = df['sentiment'].round(2)

# Save the updated dataframe to a new CSV file - overwrite the old file
df.to_csv('./DATA/bechdel_movies_with_sentiment.csv', index=False)

# Optional: Preview the first few rows to confirm changes
print(df.head())
