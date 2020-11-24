# ML-trading
Building and testing a Machine Learning-based trading algorithm

### Instrument traded:
  S&P 500 ETF - SPY

### Indicators computed: 
  1-day, 5-day percent change close in prices\
  Deviation from 5-day moving average\
  VIX - Volatility Index\
  7-day, 14-day RSI - Relative Strength Index\
  Deviation from 14-day MA of 7-day\
  7-day, 14-day MFI - Money Flow Index

### Signals generated to train data: 
  Buy: When close price is lower than in the past 5 days as well as the next 5 days\
  Sell: On the days when price is at its highest, between 2 consecutive buy signals
  
### Goal of DTC model:
  To look for and understand patterns in the given indicators and learn when to buy and sell\
  Then, use the trained model to test it on some unseen data and measure its performance to some standard banchmarks
  
### Indicators considered:
  5-day percent change close prices\
  Deviation from 5-day moving average\
  VIX - Volatility Index\
  14-day RSI\
  14-day MFI

### Train and test data: 
  Total data: January 2016 - November 2020\
  Train data: 80% ~ January 2016 - December 2019\
  Test data: 20% ~ January 2020 - November 2020

### Results:
  Accuracy: 80%\
  Model Returns: 37% in 11 month period on a starting capital of $3000\
  Benchmark returns: Buying 1 share every month and holding: 12%\
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; Investing all capital at the beginning of test period and holding: 12%
  
  Model Produced 3x the returns of typical buy and hold strategies
                     


