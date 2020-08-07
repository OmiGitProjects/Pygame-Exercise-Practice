import pygame

class Ship():
    """ Ship Setting File """
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/rocket.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """ Moving Ship """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        
        elif self.moving_down and self.rect.height > 0:
            print(self.rect.height)
            self.rect.centery += 1

        elif self.moving_up and self.rect.height < self.screen_rect.height:
            self.rect.centery -= 1

    def blitme(self):
        """ Displaying Ship on Canvas """
        self.screen.blit(self.image, self.rect)