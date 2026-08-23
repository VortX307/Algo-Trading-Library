import numpy as np
import math


def calculate(Rp : list, Rf : list, MAR : float) -> float:
    """To calculate yearly sortino ratio, enter MAR as -1 to use Rf"""
    if MAR == -1:
        MAR = Rf
        dev = _downside_deviation(Rp, MAR) 
        return (np.mean(Rp) - np.mean(Rf)) / dev * math.sqrt(252)
    elif MAR >= 0:
        dev = _downside_deviation(Rp, MAR)
        return (np.mean(Rp) - np.mean(Rf)) / dev * math.sqrt(252)
    


def calculate_curr(Rp : list, Rf : list, MAR : float) -> float:
    """To calculate sortino ratio for current time frame, enter MAR as -1 to use Rf"""
    if MAR == -1:
        MAR = Rf
        dev = _downside_deviation(Rp, MAR) 
        return (np.mean(Rp) - np.mean(Rf)) / dev
    elif MAR >= 0:
        dev = _downside_deviation(Rp, MAR)
        return (np.mean(Rp) - np.mean(Rf)) / dev 

    
def _downside_deviation(Rp, MAR):
    deviation = []
    for i in range(len(Rp)):
        if Rp[i] >= MAR:
            deviation.append(0)
        elif Rp[i] < MAR:
            diff = Rp[i] - MAR
            squared = diff ** 2
            deviation.append(squared)

    return np.mean(deviation)
    