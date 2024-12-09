'''
Hypothesis Testing
This script executes multiple methods of statistical hypothesis testing to look at relationships between variables in the Bechdel test dataset.
- Hypothesis test of Year and Bechdel score with a 2 sample t-test
- Hypothesis test of proportion of movies that pass the Bechdel test over time with a chi-square test
- Hypothesis test of Year versus Sentiment Score with a Pearson/Spearman Correlation

Running this script requires the scipy.stats and pandas libraries
'''

from scipy.stats import chi2_contingency, ttest_ind, pearsonr, spearmanr
import pandas as pd

# Load the dataset again and clean as before
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

# Drop rows with missing sentiment values
df_clean = df.dropna(subset=['sentiment'])

# 1. Hypothesis Test: Year and Passing the Bechdel Test (two-sample t-test)
pass_years = df_clean[df_clean['rating_binary'] == 1]['year']
fail_years = df_clean[df_clean['rating_binary'] == 0]['year']

# Perform two-sample t-test
t_stat_year, p_value_year = ttest_ind(pass_years, fail_years, nan_policy='omit')

# 2. Hypothesis Test: Proportion of Movies Passing the Bechdel Test Over Time (Chi-square test)
# Group by decade and count the number of movies passing/failing per decade
df_clean['decade'] = (df_clean['year'] // 10) * 10
bechdel_by_decade = df_clean.groupby(['decade', 'rating_binary'])['title'].count().unstack()

# Perform Chi-square test
chi2_stat, p_value_chi2, _, _ = chi2_contingency(bechdel_by_decade.fillna(0))
# 3. Hypothesis Test: Year vs Sentiment Score (Pearson/Spearman Correlation)
# Pearson assumes normality, while Spearman does not
pearson_corr, p_value_pearson = pearsonr(df_clean['year'], df_clean['sentiment'])
spearman_corr, p_value_spearman = spearmanr(df_clean['year'], df_clean['sentiment'])

# Output the p-values of the tests
print(f"Year and Passing Bechdel Test (t-test) p-value: {p_value_year}")
print(f"Proportion Passing Bechdel Test Over Time (Chi-square test) p-value: {p_value_chi2}")
print(f"Year vs Sentiment Score (Pearson correlation) p-value: {p_value_pearson}")
print(f"Year vs Sentiment Score (Spearman correlation) p-value: {p_value_spearman}")
