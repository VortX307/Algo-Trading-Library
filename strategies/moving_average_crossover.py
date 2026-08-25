import pandas as pd

def calculate(df : pd.DataFrame, sma_window : int, lma_window : int) -> tuple[list, int]:
    """Calculates Moving average crossover and returns a list of signal followed by calculated skip period (for price). 1 indicates long, 0 indicates hold and -1 indicates short positions"""

    sma = df["close"].rolling(window=sma_window).mean().dropna().tolist()
    lma = df["close"].rolling(window=lma_window).mean().dropna().tolist()

    skip = lma_window - sma_window
    sma = sma[skip:]

    signal = [0] #Setting first element to 0 since crossover needs prev value. Can be kept empty also

    for i in range(1, len(sma)):

        if ((sma[i - 1] < lma[i - 1]) and (sma[i] > lma[i])): #Bullish Crossover, long position
            signal.append(1)

        elif ((sma[i - 1] > lma[i - 1]) and (sma[i] < lma[i])): #Bearish Crossover, short position
            signal.append(-1)

        else: #Hold
            signal.append(0)

    return signal, lma_window
