'''
Fintech Practical Example: Stock Price Analysis and Visualization

Your team needs to analyze the daily stock prices of a fintech company ('AAPL_daily_update.csv'),
calculate summary statistics, and visualize price trends for a report.

'''

import pandas as pd
import matplotlib.pyplot as plt


# Fetch stock data for Apple (AAPL)
df = pd.read_csv('Class4/AAPL_daily_update.csv')

# Get dataset info
print(df.info())
print(df.shape)  # Dimensions
print(df.columns)  # Columns

# Access data
open_prices = df['Open']
close_prices = df['Close']

# Basic statistics
print("Max Close:", close_prices.max())
print("Min Close:", close_prices.min())
print("Mean Close:", close_prices.mean())
print("Std Dev Close:", close_prices.std())
print("Correlation:", df['Open'].corr(df['Close']))

# Lists, sets, dictionaries
price_list = list(close_prices)
unique_prices = set(price_list)
summary = {'max': max(price_list), 'min': min(price_list)}

# For and while loops, if-else, operators
for price in price_list[:5]:
    if price > 150:
        print(f"High price: {price}")
    else:
        print(f"Low price: {price}")

count = 0
while count < 3:
    print(f"Day {count + 1} close: {price_list[count]}")
    count += 1


# Create new column: daily return
df['Daily Return'] = df['Close'].pct_change()

# Filter: select days with high returns
high_return_days = df[df['Daily Return'] > 0.02]

# Remove columns/rows
df = df.drop(columns=['Adj Close'])
df = df.dropna()

# Add new row (example)
new_row = pd.DataFrame({'Open': [150], 'Close': [152], 'High': [153], 'Low': [149], 'Volume': [1000000], 'Daily Return': [0.013]}, index=[pd.Timestamp('2024-01-02')])
df = pd.concat([df, new_row])

# Export DataFrame
df.to_csv('aapl_analysis.csv')

# Plot Open and Close prices
df[['Open', 'Close']].plot(figsize=(12, 6))
plt.title('AAPL Stock Prices in 2023')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.savefig('aapl_prices.png')
plt.show()

