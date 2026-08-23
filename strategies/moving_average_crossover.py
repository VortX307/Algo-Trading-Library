import pandas as pd

def calculate(df : pd.DataFrame, sma_window : int, lma_window : int) -> tuple[list, int]:
    """Calculates Moving average crossover and returns a list of signal followed by calculated skip period. 1 indicates long, 0 indicates hold and -1 indicates short positions"""

    sma = df["close"].rolling(window=sma_window).mean().dropna().tolist()
    lma = df["close"].rolling(window=lma_window).mean().dropna().tolist()

    skip = lma_window - sma_window
    sma = sma[skip:]
    
