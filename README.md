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
  
  <img src="https://user-images.githubusercontent.com/36765231/100084469-d03ff780-2e70-11eb-824e-7d7e5594967a.png" width="600">

### Signals generated to train data: 
  Buy: When close price is lower than in the past 5 days as well as the next 5 days\
  Sell: On the days when price is at its highest, between 2 consecutive buy signals
  
### Goal of Decision Tree Classifier model:
  To look for and understand patterns in the given indicators and learn when to buy and sell\
  Then, use the trained model to test it on unseen data and measure its performance compared to some standard banchmarks
  
### Indicators considered:
  5-day percent change close prices\
  Deviation from 5-day moving average\
  VIX - Volatility Index\
  14-day RSI\
  14-day MFI
  
  <img src="https://user-images.githubusercontent.com/36765231/100086499-84428200-2e73-11eb-8626-ef1f93a34db7.png" width="600">

### Train and test data: 
  Total data: January 2016 - November 2020\
  Train data: 80% ~ January 2016 - December 2019\
  Test data: 20% ~ January 2020 - November 2020

### Results:
  <img src="https://user-images.githubusercontent.com/36765231/100085468-147fc780-2e72-11eb-9592-ac30e288ffe3.png" width="800">
  
  Accuracy: 80%\
  Model Returns: 37% in 11 month period on a starting capital of $3000\
  Benchmark returns: Buying 1 share every month and holding: 12%\
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; Investing all capital at the beginning of test period and holding: 12%
  
  Visualization and returns of the buy and hold strategy
  
  <img src="https://user-images.githubusercontent.com/36765231/100084287-95d65a80-2e70-11eb-93ac-c0b1ee2d9a3f.png" width="800">


