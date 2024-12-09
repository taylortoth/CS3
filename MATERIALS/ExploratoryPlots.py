'''
Exploratory Plots
    This script executes exploratory plots based on our dataset, focusing on their release years, Bechdel test ratings, visibility status, and sentiment scores.
    To visualize the distributions and relationships between the variables, this script outputs various plots using Seaborn. The plots are output as PNGs in a 
    specified folder.

    Ensure the dataset 'bechdel_movies.csv' is available in your chosen directory. When the script is executed, the directory './OUTPUT/Exploratory/' will be 
    created to save the visualizations. This script utilizes the following libraries: pandas, matplotlib, seaborn, and os.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV into dataframe
df = pd.read_csv('./DATA/bechdel_movies.csv')

# Set Seaborn style - aesthetic purposes
sns.set(style="whitegrid")

# Create a directory to save the plots
output_folder = './OUTPUT/Exploratory/'
import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 1. Distribution of movie release years with histogram and KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['year'], bins=30, kde=True, color='blue')
plt.title('Distribution of Movie Release Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.savefig(f'{output_folder}DistributionofMovieReleaseYears.png')
plt.close()

# 2. Distribution of Bechdel test ratings using a count plot
plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=df, palette='coolwarm')
plt.title('Distribution of Bechdel Test Ratings', fontsize=16)
plt.xlabel('Bechdel Test Rating', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig(f'{output_folder}DistributionofBechdelRatings.png')
plt.close()

# 3. Distribution of sentiment scores with histogram and KDE
plt.figure(figsize=(10, 6))
sns.histplot(df['sentiment'], bins=30, kde=True, color='green')
plt.title('Distribution of Sentiment Scores', fontsize=16)
plt.xlabel('Sentiment Score', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.savefig(f'{output_folder}DistributionofSentimentScores.png')
plt.close()

# 4. Joint plot of Year vs Sentiment Score - results in a scatterplot
plt.figure(figsize=(8, 8))
sns.jointplot(x='year', y='sentiment', data=df, kind='scatter', color='purple', height=8)
plt.savefig(f'{output_folder}YearvsSentimentScore.png')
plt.close()

# 5. Count of movies by visibility status; 1 = visible, 0 = not visible
plt.figure(figsize=(10, 6))
sns.countplot(x='visible', data=df, palette='viridis')
plt.title('Count of Movies by Visibility Status', fontsize=16)
plt.xlabel('Visible (1 = Yes, 0 = No)', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.savefig(f'{output_folder}CountofMoviesbyVisibility.png')
plt.close()

# 6. Movies that pass (rating == 3) vs those that fail (rating < 3)

# Create a new column to indicate whether movies pass or fail the Bechdel test
df['test_result'] = df['rating'].apply(lambda x: 'Pass' if x == 3 else 'Fail')
# count plot of passing or failing the Bechdel test
plt.figure(figsize=(10, 6))
sns.countplot(x='test_result', data=df, palette='coolwarm')
plt.title('Movies That Pass vs Fail the Bechdel Test', fontsize=16)
plt.xlabel('Test Result', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.savefig(f'{output_folder}PassOrFailBechdel.png')
plt.close()

# 7. Movies that pass the Bechdel test over time (entire dataset)
plt.figure(figsize=(12, 6))
df_pass = df[df['rating'] == 3]
sns.histplot(df_pass['year'], bins=40, kde=False, color='green')
plt.title('Movies That Pass the Bechdel Test (All Years)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.savefig(f'{output_folder}MoviesThatPassBechdel.png')
plt.close()

# 8. Colorful pair plot with title - examine relationship between year, rating, and sentiment
plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(df[['year', 'rating', 'sentiment']], hue='rating', palette='coolwarm', diag_kind="kde", markers=["o", "s", "D", "P"])
plt.suptitle('Relationships Between Year, Rating, and Sentiment', y=1.02, fontsize=16)
pair_plot.savefig(f'{output_folder}PairPlotYearSentimentRating.png')
plt.close()

# 9. Count of Bechdel test ratings (0, 1, 2, 3) - see annotations below
plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=df, palette='coolwarm')
plt.title('Distribution of Bechdel Test Ratings', fontsize=16)
plt.xlabel('Bechdel Test Rating', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)

# Annotate the plot with the meaning of each rating
annotations = {
    0: "Does not have at least two named women",
    1: "Has at least two named women",
    2: "Women talk to each other",
    3: "Women talk to each other about something besides a man"
}

for rating, explanation in annotations.items():
    plt.text(rating, df['rating'].value_counts().loc[rating] + 10, explanation,
             ha='center', fontsize=10)

plt.tight_layout() # adjust for better fit
plt.savefig(f'{output_folder}AnnotatedBechdelTestRatings.png')
plt.close()
