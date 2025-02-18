import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = random.choices(string.ascii_uppercase, k = 9)



    def is_valid(self, word : str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        grid_copy = self.grid.copy()
        if not word:
            return False

        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False
        return True




if __name__ == '__main__':
    print(random.choices(string.ascii_uppercase, k = 9))
