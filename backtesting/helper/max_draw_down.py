def calculate(returns : list) -> float:
    """To calculate the max draw down of portfolio over lifetime"""
    peak = 1.0
    value = 1.0
    drawdown = [0]

    for i in range(len(returns)):
        value *= (returns[i] + 1)

        if value >= peak:
            peak = value
        elif value < peak:
            drawdown.append((value - peak) / peak)


    return min(drawdown)
