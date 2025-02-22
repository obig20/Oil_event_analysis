from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from pmdarima import auto_arima
import pandas as pd

def fit_arima(series):
    """Automated ARIMA fitting"""
    return auto_arima(series, seasonal=False, suppress_warnings=True)

def fit_garch(returns):
    """GARCH volatility modeling"""
    return arch_model(returns * 100, vol='GARCH', p=1, q=1).fit(disp='off')

def calculate_impacts(df, events, window=30):
    """Event impact analysis"""
    impacts = []
    for _, event in events.iterrows():
        try:
            idx = df.index.get_loc(event['Date'], method='nearest')
            pre = df.iloc[idx-window:idx]
            post = df.iloc[idx:idx+window]
            impacts.append({
                'Event': event['Event'],
                'Date': df.index[idx].date(),
                'Price_Change': post['Price'][-1] - pre['Price'][0],
                'Volatility_Change': post['Returns'].std() - pre['Returns'].std()
            })
        except KeyError:
            continue
    return pd.DataFrame(impacts)