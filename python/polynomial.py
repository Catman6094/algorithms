class Polynomial:
    def __init__(self, C) -> None:
        self.coefficients = C
    
    def __len__(self):
        return len(self.coefficients)
    
    def __call__(self, x):
        # Horner's rule
        y = 0
        for i in range(len(self) - 1, -1, -1):
            y = self.coefficients[i] + x * y
        return y


if __name__ == "__main__":
    p = Polynomial([1, 2, 3, 4])
    assert p(0) == 1
    assert p(1) == 10
    assert p(3) == 142