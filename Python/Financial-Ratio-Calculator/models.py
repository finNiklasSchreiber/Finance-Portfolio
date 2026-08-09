class FinancialMetric:

    def __init__(self, current, previous):
        self.current = current
        self.previous = previous

class FinancialData:
    def __init__(self):
        self.revenue = None
        self.gross_profit = None
        self.operating_income = None
        self.net_income = None
        self.free_cash_flow = None