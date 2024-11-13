
# Import necessary libraries
from urllib.request import urlopen, Request  # For opening URLs and making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # For sentiment analysis
import pandas as pd  # For data manipulation and analysis
from datetime import date, datetime  # For working with dates
import matplotlib.pyplot as plt  # For plotting data

# Define the URL and a list of stock ticker symbols to analyze
finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB']

# Initialize a dictionary to store news tables for each ticker
news_tables = {}

# Loop through each ticker symbol to fetch news data
for ticker in tickers:
    # Construct the URL for the stock's news page
    url = finviz_url + ticker

    # Set up a request to avoid access denial (User-Agent trick)
    req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)  # Open the URL and get the response

    # Parse the HTML content using BeautifulSoup
    html = BeautifulSoup(response, features='html.parser')

    # Find the news table by its HTML element ID
    news_table = html.find(id='news-table')

    # Store the news table in the dictionary
    news_tables[ticker] = news_table

    # Break after first ticker for testing (remove in final version)
    break

# Initialize a list to store parsed news data
parsed_data = []

# Placeholder for the current date
currdate = "Sept-25-24"

# Process each ticker and its corresponding news table
for ticker, news_table in news_tables.items():

    # Loop through each row in the news table
    for row in news_table.findAll('tr'):

        # Extract the news title
        title = row.a.text

        # Split date and time information
        date_data = row.td.text.split(' ')

        # Process 'Today' or set date based on the date format in HTML
        if date_data[13] != '' and date_data[12] == "Today":
            time = date_data[13]
            datee = currdate  # Use current date placeholder for 'Today'
        elif date_data[13] != '':
            time = date_data[13]
            datee = date_data[12]  # Use the provided date if not 'Today'
            currdate = datee  # Update placeholder for current date
        else:
            datee = currdate  # If no date, use current date
            time = date_data[12]

        # Append parsed data as a list of [ticker, date, time, title]
        parsed_data.append([ticker, datee, time, title])

# Create a DataFrame from the parsed data
df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

# Initialize sentiment analyzer
vader = SentimentIntensityAnalyzer()

# Apply sentiment analysis on each title and create a new 'compound' column
f = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(f)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df.date).dt.date

# Plotting the average sentiment per day
plt.figure(figsize=(10, 8))  # Set the plot size

# Group by date and calculate the mean sentiment score for each day
mean_df = df.groupby(['date'])['compound'].mean()

# Display the head of the grouped data
print(mean_df.head())

# Plot the sentiment trend as a bar chart
mean_df.plot(kind='bar')
plt.show()





