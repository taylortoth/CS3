# CS3
DS4002 CS3

This GitHub repository contains all the information needed to replicate my project that used text data to analyze the Bechdel test and sentiment score information over time. 

## Section 1 - Software and Platform

The main software used for this project includes Google Colab with Python and VS Code with Python. We used Python's **requests** and **BeautifulSoup** packages to scrape movie reviews from IMDb, and the **VADER SentimentIntensityAnalyzer** package to analyze the text reviews and derive sentiment scores. 

The original coding was performed on a Windows machine, with some portions done using a Mac.

## Section2: Map of Documentation

### Project Folder Structure: 

```
CS3/
│
├── HOOK&RUBRIC
│   ├── hook.pdf
│   └── rubric.csv 
│
├── MATERIALS/
│   ├── ANALYSISPLOTS/
│   │   ├── AverageSentimentScoreOverTime.png
│   │   ├── HeatmapNumericalFeatures.png
│   │   ├── PassByDecade.png
│   │   ├── PassFailvsSentimentScore.png
│   │   ├── ProportionOfMoviesPassingOverTime.png
│   │   ├── ScoreOfMoviesPassingVersusFailingOverTime.png
│   │   └── SentimentOverTimeBoxplot.png
|   ├── CODE/
│   │    ├── AddBinaryRating.py
│   │    ├── AnalysisPlots.py
│   │    ├── ExploratoryPlots.py
│   │    ├── HypothesisTesting.py
│   │    ├── HypothesisTestingTime.py
│   │    ├──IMDbReviewSentiment.py
│   │    ├── LogisticRegression.py
│   │    ├── RoundSentiment.py
│   |    └── ScrapeNewBechdel.py
│   ├── DATA
│   │     ├── bechdel_movies.csv
│   │     ├── bechdel_movies_combined.csv
│   │     └── bechdel_movies_with_sentiment.csv
│   └── Exploratory/
│   │   ├── DistributionofBechdelRatings.png
│   │   ├── DistributionofSentimentScores.png
│   │   ├── MoviesThatPassBechdel.png
│   │   ├── PairPlotYearSentimentRating.png
│   │   ├── PassOrFailBechdel.png
│   │   └── YearvsSentimentScore.png
│   └── blog.pdf/
│
├── LICENSE.md
└── README.md
```
- **HOOK&RUBRIC/**:
  - This is where you find the hook document that will give information on the context of the case study that is to go alongside this repository. The rubric you are to follow is here and should answer all questions on how to successfully replicate the given case study. 
- **MATERIALS/**:
  - The materials folder contains four subfolders: analysis plots, example code, data, and exploratory plots. These subfolders contain the different transformations the data will go through, the code to perform all the analysis, and examples of exploratory and final plots. The blog document gives further detail into the project, background information to assist in evaluation, and useful websites. Additional references will be listed at the bottom of the page.
 
## Important Refernces

[1] “vaderSentiment,” PyPI, Apr. 23, 2018. https://pypi.org/project/vaderSentiment/.

[2] “Bechdel Test Movies,” kaggle.com.
https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023

[3] Shih, J. (2024, July 3).Interpreting the score and ratio of sentiment analysis. Twinword.
https://www.twinword.com/blog/interpreting-the-score-and-ratio-ofsentiment/#:~:text=The%20score%20indicates%20how%20negative,inclusively%2C%20we%20tag%20as%20neutral

[4] J. Light, “What Is the Bechdel Test and How Will It Help Your Writing?,” nofilmschool.com, 
Jan. 25, 2024. https://nofilmschool.com/bechdel-test

[5] “Bechdel Test Movie List” bechdeltest.com
https://bechdeltest.com/
