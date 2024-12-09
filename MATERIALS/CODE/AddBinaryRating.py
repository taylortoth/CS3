'''
Add Binary Ratings in Bechdel Dataset
  Running this script will result in loading a dataset of movies including sentiment scores from IMDb reviews. For further analysis, simplify the 'rating' column into binary 
  classification: 1 for pass (rating == 3), 0 for fail (rating != 3). Additionally, the updated dataset is saved to the same CSV file, 'bechdel_movies.csv'. You can also check the 
  distribution of the new binary 'rating_binary' column dataset to confirm that the proper changes were made.

  This script only requires the pandas library.
'''
import pandas as pd

df = pd.read_csv('./DATA/bechdel_movies.csv')

# Simplify the 'rating' column into binary classification: 1 for pass (rating == 3), 0 for fail (rating != 3)
df['rating_binary'] = df['rating'].apply(lambda x: 1 if x == 3 else 0)

# Drop rows with missing sentiment values
df_clean = df.dropna(subset=['sentiment'])

# Check the distribution of the new binary 'rating_binary' column
df_clean['rating_binary'].value_counts()

df.to_csv('./DATA/bechdel_movies.csv', index=False)
