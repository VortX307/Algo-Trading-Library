def calculate(equity_curve : list) -> list:
    """To calculate the returns based on equity curve."""
    returns = []
    for i in range(len(equity_curve) - 1):
        returns.append((equity_curve[i+1] - equity_curve[i]) / equity_curve[i])

    return returns
