import pandas as pd

# We read in a stock data data file into a data frame and see what it looks like
df = pd.read_csv('./GOOG.csv')

# We load the Google stock data into a DataFrame
google_stock = pd.read_csv('./GOOG.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv('./AAPL.csv', index_col = ['Date'], parse_dates=['Date'], usecols = ['Date', 'Adj Close'])

# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv('./AMZN.csv', index_col = ['Date'], parse_dates=['Date'], usecols = ['Date', 'Adj Close'])

# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index=dates)

# Change the Adj Close column label to Google
google_stock = google_stock.rename({'Adj Close': 'Google'})

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename({'Adj Close': 'Apple'})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename({'Adj Close': 'Amazon'})

# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

# Check if there are any NaN values in the all_stocks dataframe
all_stocks.isnull().any()

# Remove any rows that contain NaN values
all_stocks.dropna(axis=0, inplace=True)

# Print the average stock price for each stock
print(all_stocks.mean())

# We compute the rolling mean using a 150-Day window for Google stock
rollingMean = all_stocks['Google'].rolling(150).mean()