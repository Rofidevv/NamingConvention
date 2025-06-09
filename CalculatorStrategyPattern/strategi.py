from abc import ABC, abstractmethod

# Interface Strategy (Bagian 1)
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass

# Implementasi Strategi (Bagian 2)
class AddOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a + b

class SubtractOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a - b

class MultiplyOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a * b

class DivideOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol.")
        return a / b