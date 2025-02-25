import pandas as pd

def load_prices(file_path):
    """
    Load and clean oil price data
    Args:
        file_path (str): Path to CSV file with columns 'Date' and 'Price'
    Returns:
        pandas.DataFrame: Cleaned DataFrame with datetime index
    """
    df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df = df.set_index('Date').sort_index()
    
    # Handle missing dates (weekends/holidays)
    df = df.asfreq('D').ffill()
    
    return df[['Price']]

def load_events(file_path):
    """
    Load geopolitical events data
    Args:
        file_path (str): Path to CSV file with columns 'Date' and 'Event'
    Returns:
        pandas.DataFrame: DataFrame with event dates and descriptions
    """
    events = pd.read_csv(file_path, parse_dates=['Date'])
    return events[['Date', 'Event']]