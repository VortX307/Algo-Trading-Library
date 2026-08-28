import pandas as pd


def calculate(df : pd.Dataframe, period : int) -> list:
    """Calculate donchian chanel breakout strategy signal. Remember skip = input period."""
    
    df["upper"] = df["high"].rolling(period).max().shift(1)
    df["lower"] = df["low"].rolling(period).min().shift(1)

    df = df.dropna().reset_index(drop=True)

    df["signal"] = 0

    df.loc[df["close"] > df["upper"], "signal"] = 1 #Above current high

    df.loc[df["close"] < df["lower"], "signal"] = -1 #Below prev low

    signal = df["signal"].tolist()

    return signal