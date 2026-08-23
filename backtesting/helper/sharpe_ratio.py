import numpy as np
import math


def calculate(Rp : list, Rf : list) -> float:
    """To calculate yearly sharpe ratio."""
    result = [a-b for a, b in zip(Rp, Rf)]
    return ((np.mean(Rp) - np.mean(Rf)) / np.std(result)) * math.sqrt(252)

def calculate_curr(Rp : list, Rf : list) -> float:
    """To calculate sharpe ratio based on current time frame."""
    result = [a-b for a, b in zip(Rp, Rf)] 
    return (np.mean(Rp) - np.mean(Rf)) / np.std(result)
