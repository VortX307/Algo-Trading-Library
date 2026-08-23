class Broker():
    """To place trades, calculate equity and number of shares."""
    def __init__(self, signal : int, price : float, state : bool, cash = 0.0, shares = 0):
        """Initialize the broker with signal, price, state, cash and shares."""
        self.price = price
        self.cash = cash
        self.shares = shares
        self.signal = signal
        self.state = state
        
    def buy(self) -> tuple[int, float]:
        """For buying shares\n
        Input: Share price(float), Money in account(float)
        Output: Shares bought (int), money left(float)"""

        shares = int(self.cash // self.price)
        left = self.cash - (shares * self.price)

        return shares, left


    def sell(self) -> float:
        """For selling shares\n
        Input: Share price(float), Number of shares(int)
        Output: Money added to portfolio(float)"""

        return self.shares * self.price

    def execute(self) -> list[float, int, bool]:
        """To execute the broker. Call this function to execute a trade."""
        if self.signal == 0:
            return self.price * self.shares + self.cash, self.shares, self.state
        elif self.signal == 1:
            shares, left = self.buy()
            self.state = True
            return shares * self.price + left, shares, self.state
        elif self.signal == -1:
            money = self.sell()
            self.state = False
            return money, 0, self.state
        