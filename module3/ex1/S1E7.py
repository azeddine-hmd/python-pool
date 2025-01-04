from S1E9 import Character


class Baratheon(Character):
    """Representing the Barratheon family."""

    def __init__(self, first_name, is_alive=True):
        """constructor for Baratheon class"""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @classmethod
    def create_baratheon(cls, first_name: str, is_alive=True):
        """create baratheon character"""
        return cls(first_name, is_alive)

    def __str__(self):
        """return representation of instance to string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """return representation of instance to string"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        """constructor for Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        """create lannister character"""
        return cls(first_name, is_alive)

    def __str__(self):
        """return representation of instance to string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """return representation of instance to string"""
        return self.__str__()
