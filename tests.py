import unittest
from settings import Settings


class TestSettings(unittest.TestCase):
    """Tests the settings for AlienInvasion"""

    def setUp(self):
        """attributes for settings"""
        self.settings = Settings()
    
    def test_screen_width(self):
        """Tests default screen width"""
        self.assertEqual(self.settings.screen_width, 1200)

    def test_screen_bg_color(self):
        """Tests background color"""
        self.assertEqual(self.settings.bg_color,(230,230,230))

"""
Cannot test run_game() because terminal gets blocked

class TestAlienInvasion(unittest.TestCase):
    

    def setUp(self):
        self.ai = AlienInvasion()

    def test_run_game(self):
        
        self.assertEqual(self.screen.fill(self.settings.bg_color),self.screen.fill((230,230,230)))
"""

if __name__ == "__main__":
    unittest.main()