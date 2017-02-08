import pygame

class Sprite(pygame.sprite.Sprite):
    #need for speed
    speed = 5
    uSpeed = 0
    rSpeed = 0
    dSpeed = 0
    lSpeed = 0
    destructable = False

    def __init__(self, sprite, startx, starty, width, height):
        super().__init__()

        self.width = width
        self.height = height

        #set the image
        self.image = pygame.image.load(sprite)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #set the starting location
        self.rect.topleft = [startx, starty]

        #scale the image down to a manageable size
        self.image = pygame.transform.smoothscale(self.image, (width, height))

        targetRect = pygame.Rect(startx, starty, width, height)
        #scale hitbox to new size
        self.rect = self.rect.clip(targetRect)