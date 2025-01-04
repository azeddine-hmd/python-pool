from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """the king."""

    def __init__(self, first_name: str, is_alive=True):
        """constructor for King class"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """set the eyes color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """set the hair color"""
        self.hairs = color

    def get_eyes(self):
        """get the eyes color"""
        return self.eyes

    def get_hairs(self):
        """get the eyes color"""
        return self.hairs
