class calculator:
    """performs calculations on a vector"""

    def __init__(self, vector: list):
        """constructor for calculator class"""
        self.vector = vector

    def __add__(self, object) -> None:
        """addition overload function"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiplication overload function"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """substraction overload function"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """true division overload function"""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print("Error:", e)
