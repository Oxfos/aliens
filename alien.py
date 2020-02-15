import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to model the alien"""

    def __init__(self, ai_game):
        """Initialization of an ALien instance"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien right or left."""
        # Use update()-internal float x to assign alien.rect.x
        # and do not take alien.rect.x otherwise you cannot accept alien
        # speeds lower than 1 because they will always be int()-ed >> 0
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        """
        My solution: I add a moving operation in y direction similar to 
        moving in x direction with a switch operator:
        """
        self.rect.y += self.settings.fleet_drop * self.settings.drop_switch
