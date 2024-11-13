<----Leveraging Beautiful Soup for Sentiment Analysis---->

  1.Import necessary libraries for web scraping, data manipulation, date handling, sentiment analysis, and plotting.

  2. Set up variables by defining the base URL for news scraping (finviz_url) and a list of stock tickers (e.g., ['AMZN', 'GOOG', 'FB']) to analyze. Initialize an empty dictionary, news_tables, to store scraped          news data for each ticker.

  3. Fetch news data for each ticker by looping through each ticker in the tickers list:

  4.Construct the URL for the specific ticker, create an HTTP request with a browser-like User-Agent header, open the URL, and retrieve HTML content.
    Parse the HTML content using BeautifulSoup, locate the news table element by its HTML ID (news-table), and store the news table in the news_tables dictionary with the ticker as the key.
    Initialize an empty list parsed_data to store structured news data. Loop through each ticker and its news table in news_tables. For each row in the news table:

  5.Extract the news title, split the date and time information into a list (date_data), and use conditional checks to manage different date formats:
    If the date data indicates "Today," set the current date from a placeholder variable (currdate).
    Otherwise, use the provided date, update currdate, and store the appropriate date and time values in parsed_data as [ticker, date, time, title].
    Convert parsed data to a DataFrame by creating df from parsed_data with columns ['ticker', 'date', 'time', 'title'].

  6. Initialize the Vader Sentiment Intensity Analyzer to perform sentiment analysis. Define a lambda function to calculate the compound sentiment score for each news title using vader.polarity_scores. Apply this        function to the title column in df and create a new column compound to store each title’s sentiment score.

  7. Format the date column by converting df['date'] to a datetime format.

  8. Calculate the average sentiment score per date by grouping df by date and computing the mean compound sentiment score for each day.

  9. Plot the sentiment trend over time by creating a bar chart with dates on the x-axis and average sentiment scores on the y-axis, displaying the sentiment trend for each date.
