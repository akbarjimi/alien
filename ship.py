import pygame


class Ship:
    def __init__(self, game):
        self.setGame(game)
        self.initial()

    def initial(self):
        self.image = pygame.transform.flip(pygame.image.load('images/ship.png'), False, True)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.getGame().getSurface().get_rect().midbottom
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def setGame(self, game):
        self.game = game

    def getGame(self):
        return self.game

    def update(self):
        if self.move_right and self.rect.right < self.getGame().getSurface().get_rect().right:
            self.x += self.getGame().getSettings().getSpeed()

        if self.move_left and self.rect.left > 0:
            self.x -= self.getGame().getSettings().getSpeed()

        if self.move_up and self.rect.top > 0:
            self.y -= self.getGame().getSettings().getSpeed()

        if self.move_down and self.rect.bottom <= self.getGame().getSurface().get_rect().bottom:
            self.y += self.getGame().getSettings().getSpeed()

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.getGame().getSurface().blit(self.image, self.rect)
