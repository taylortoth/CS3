'''
Generating Analysis Plots
This script loads the data from bechdel_movies.csv and cleans it. Then subsets of the data are created to ease the process of generating plots.

Running this script requires the pandas and matplotlib.pyplot libraries.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset again and clean as before
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

# Drop rows with missing sentiment values
df_clean = df.dropna(subset=['sentiment'])

# Load and prepare data (assuming df_clean is already cleaned)
df_clean['year'] = pd.to_numeric(df_clean['year'], errors='coerce')

# 1. Proportion of Movies Passing the Bechdel Test by Decade
df_clean['decade'] = (df_clean['year'] // 10) * 10
bechdel_by_decade = df_clean.groupby('decade')['rating_binary'].mean()

plt.figure(figsize=(10, 6))
bechdel_by_decade.plot(kind='bar', color='skyblue')
plt.title('Proportion of Movies Passing the Bechdel Test by Decade', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Proportion Passing', fontsize=12)
plt.grid(axis='y', linestyle='--')
plt.xticks(rotation=45)
plt.show()
# 2. Distribution of Sentiment Scores (KDE plot)
plt.figure(figsize=(10, 6))
df_clean[df_clean['rating_binary'] == 1]['sentiment'].plot(kind='kde', color='green', label='Passing', linewidth=2)
df_clean[df_clean['rating_binary'] == 0]['sentiment'].plot(kind='kde', color='red', label='Failing', linewidth=2)
plt.title('Distribution of Sentiment Scores for Movies Passing vs Failing', fontsize=14)
plt.xlabel('Sentiment Score', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 3. Boxplots of Sentiment Scores Over Time
df_clean['decade'] = pd.cut(df_clean['year'], bins=range(1870, 2030, 10), right=False, labels=[f"{x}s" for x in range(1870, 2020, 10)])

plt.figure(figsize=(12, 8))
df_clean.boxplot(column='sentiment', by='decade', grid=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Boxplot of Sentiment Scores Over Time', fontsize=14)
plt.suptitle('')
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Sentiment Score', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 4. Movie Count per Year
plt.figure(figsize=(10, 6))
df_clean.groupby('year')['title'].count().plot(kind='line', color='purple', linewidth=2)
plt.title('Number of Movies Evaluated for Bechdel Test Per Year', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.grid(True)
plt.show()
# 5. Correlation Heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = df_clean[['year', 'sentiment', 'rating_binary']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap for Year, Sentiment, and Bechdel Test Score', fontsize=14)
plt.show()
