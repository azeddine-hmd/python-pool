class calculator:
    """performs calculations on a vector"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product operation on two vectors"""
        print("Dot product is:", sum(x * y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """addition operation on two vectors"""
        print("Add vector is:", [float(x + y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substraction operation on two vectors"""
        print("Sous vector is:", [float(x - y) for x, y in zip(V1, V2)])
