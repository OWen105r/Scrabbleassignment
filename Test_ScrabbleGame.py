import unittest
from scrabble_game import scrabble_score # type: ignore

class TestScrabbleScore(unittest.TestCase):
    # Requirement 1: The numbers are added up correctly for a given word
    def test_single_letter(self):
        self.assertEqual(scrabble_score('A'), 1)
        self.assertEqual(scrabble_score('Z'), 10)

    def test_word(self):
        self.assertEqual(scrabble_score('cabbage'), 14)
        self.assertEqual(scrabble_score('Scrabble'), 14)

    def test_mixed_case(self):
        self.assertEqual(scrabble_score('CaBbAgE'), 14)
     
    # Requirement 2: Upper- and lower-case letters should have the same value
    def test_uppercase(self):
        self.assertEqual(scrabble_score('CABBAGE'), 14)

    def test_lowercase(self):
        self.assertEqual(scrabble_score('cabbage'), 14)

    # Requirement 3: Prompt user with the right feedback if user does not enter an alphabet
    def test_invalid_input(self):       
        self.assertEqual(scrabble_score('123'), 0)
        self.assertEqual(scrabble_score('<>?"'), 0)
        self.assertEqual(scrabble_score(''), 0)
        self.assertEqual(scrabble_score(' '), 0)

    # Requirement 4: Timer functionality
    def test_timer_functionality(self):
        
        import time
        start_time = time.time()
        time.sleep(1)  # Simulate delay
        end_time = time.time()
        self.assertTrue(end_time - start_time >= 1)
    
    def test_word_length_check(self):
        word = 'cabbage'
        word_length = 7
        self.assertEqual(len(word), word_length)

    def test_score_based_on_time(self):
        word = 'cabbage'
        score = scrabble_score(word)
        time_taken = 10  # Simulate time taken in seconds
        bonus = max(0, 30 - time_taken)  # Bonus points for faster input
        total_score = score + bonus
        self.assertEqual(total_score, 14 + 20)

    
    # Requirement 5: Ensure word is valid
    def test_dictionary_word_validation(self):
        valid_words = ['cabbage', 'scraBBle', 'APPLE']
        invalid_words = ['123', 'azxc1213', '?><+#}']
        for word in valid_words:
            self.assertTrue(word.isalpha())
        for word in invalid_words:
            self.assertFalse(word.isalpha())

    def test_no_score_for_invalid_words(self):
        invalid_words = ['890', 'abmnd12@d', '!@#']
        for word in invalid_words:
            self.assertEqual(scrabble_score(word), 0)


    # Requirement 6: Game keeps going until player quits or after 10 rounds
    def test_game_continues(self):
        rounds = 10
        total_score = 0
        for _ in range(rounds):
            word = 'red'
            score = scrabble_score(word)
            total_score += score
        self.assertEqual(total_score, 4 * rounds)

    def test_game_quit(self):
        rounds = 5 # Simulate the player quitting the game
        total_score = 0
        for _ in range(rounds):
            word = 'cabbage'
            score = scrabble_score(word)
            total_score += score
        self.assertEqual(total_score, 14 * rounds)

if __name__ == '__main__':
    unittest.main()