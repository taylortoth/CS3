# CS3
DS4002 CS3

This GitHub repository contains all the information needed to replicate my project that used text data to analyze the Bechdel test and sentiment score information over time. 

## Section 1 - Software and Platform

The main software used for this project includes Google Colab with Python and VS Code with Python. We used Python's **requests** and **BeautifulSoup** packages to scrape movie reviews from IMDb, and the **VADER SentimentIntensityAnalyzer** package to analyze the text reviews and derive sentiment scores. 

The original coding was performed on a Windows machine, with some portions done using a Mac.

## Section2: Map of Documentation

### Project Folder Structure: 

'''
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
│       ├── DistributionofBechdelRatings.png
│       ├── DistributionofSentimentScores.png
│       ├── MoviesThatPassBechdel.png
│       ├── PairPlotYearSentimentRating.png
│       ├── PassOrFailBechdel.png
│       └── YearvsSentimentScore.png
│
├── LICENSE.md
└── README.md
```
