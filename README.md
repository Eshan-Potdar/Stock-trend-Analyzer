# Stock Trend Analyzer

## Overview

Stock Trend Analyzer is a Python-based financial analysis tool that evaluates stock market trends using historical data from Yahoo Finance.

The program downloads two years of stock price data for a user-specified company and analyzes it using technical indicators such as Moving Average, Momentum, and Volatility. Based on these indicators, the program classifies the stock's current market trend.

## Features

* Downloads historical stock data using Yahoo Finance
* Calculates 20-Day Moving Average (MA20)
* Calculates 20-Day Momentum
* Calculates 20-Day Volatility
* Classifies stock trends into:

  * Strong Uptrend
  * Weak Uptrend
  * Strong Downtrend
  * Weak Downtrend
  * Uncertain
* Handles invalid ticker symbols

## Technologies Used

* Python
* yfinance
* pandas
* numpy

## How It Works

The program performs the following steps:

1. Accepts a stock ticker symbol from the user.
2. Downloads two years of historical stock price data.
3. Calculates:

   * 20-Day Moving Average
   * 20-Day Momentum
   * 20-Day Volatility
4. Evaluates the stock using predefined trend rules.
5. Displays a trend signal and supporting metrics.

## Example

Input:

```text
AAPL
```

Output:

```text
Trend Signal: Strong Uptrend

Price: 210.45
MA20: 205.30
Momentum: 0.0620
Volatility: 0.0154
```

## Installation

Install the required libraries:

```bash
pip install yfinance pandas numpy matplotlib
```

## Running the Program

```bash
python stock_trend_analyzer.py
```

Enter a ticker symbol when prompted:

```text
Enter the Ticker of the Company: AAPL
```

## Future Improvements

* Compare multiple stocks
* Add graphical visualizations
* Generate buy/sell recommendations
* Build a graphical user interface (GUI)
* Include additional technical indicators

## Author

Eshan Potdar
