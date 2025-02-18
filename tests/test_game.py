from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            game = Game()

            # exercise
            grid = game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

            # teardown

    def test_game_invalid_empty_word(self):

        #setup
        game = Game()

        #exercice

        #verify
        assert game.is_valid('') is False


    def test_game_valid_word(self):

        #setup
        game = Game()

        test_grid = ['K','W','E','U','E','A','K','R','Z']
        test_word = 'EUREKA'
        game.grid = test_grid

        #verify
        assert game.is_valid(test_word) is True

        #teardown
        assert game.grid == list(test_grid) # Make sure the grid remained untouched


    def test_game_invalid_word(self):

        #setup
        game = Game()

        test_grid = ['K','W','E','U','E','A','K','R','Z']
        test_word = 'EUREPA'
        game.grid = test_grid

        #verify
        assert game.is_valid(test_word) is False

        #teardown
        assert game.grid == list(test_grid) # Make sure the grid remained untouched
