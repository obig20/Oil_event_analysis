import matplotlib.pyplot as plt

def plot_prices(df):
    """Plot price trends"""
    fig, ax = plt.subplots(figsize=(14, 6))
    df['Price'].plot(ax=ax, title='Brent Crude Oil Prices')
    ax.set_ylabel('USD/Barrel')
    return fig

def plot_volatility(df):
    """Plot volatility analysis"""
    fig, ax = plt.subplots(figsize=(14, 6))
    df['Returns'].rolling(30).std().plot(ax=ax, color='red')
    ax.set_title('30-Day Rolling Volatility')
    return fig