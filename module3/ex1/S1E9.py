from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class of Character"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """constructor for Character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """kill character"""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive=True):
        """constructor for stark class"""
        super().__init__(first_name, is_alive)
