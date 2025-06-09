from strategi import OperationStrategy

# Context (Bagian 3)
class Calculator:
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a: int, b: int) -> float:
        return self.strategy.execute(a, b)