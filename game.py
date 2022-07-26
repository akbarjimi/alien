import sys
import pygame
from ship import Ship
from settings import Settings


class Game:
    settings: Settings
    ship: None|Ship

    def __init__(self, settings: Settings):
        self.ship = None
        self.setSettings(settings)
        self.initial()
        self.setDimension()
        self.getSettings().setWidth(self.getSurface().get_rect().width)
        self.getSettings().setHeight(self.getSurface().get_rect().height)

    def setSettings(self, settings: Settings):
        self.settings = settings

    def getSettings(self) -> Settings:
        return self.settings

    def initial(self):
        pygame.init()
        pygame.display.set_caption(self.getSettings().getCaption())

    def setDimension(self):
        self.setSurface(
            surface=pygame.display.set_mode(self.getSettings().goFullScreen(), pygame.FULLSCREEN)
        )

    def setSurface(self, surface):
        self.surface = surface

    def getSurface(self):
        if not self.surface:
            raise RuntimeError
        return self.surface

    def getShip(self) -> Ship:
        if not self.ship:
            self.ship = Ship(self)
        return self.ship

    def run(self):
        while True:
            self._check_events()
            self.getShip().update()
            self._update_screen()

    def _update_screen(self):
        self.getSurface().fill(self.getSettings().getLightGreen())
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self._handle_key_up(event)

    def _handle_key_up(self, event):
        self.goRight(event, False)
        self.goLeft(event, False)
        self.goUp(event, False)
        self.goDown(event, False)

    def _handle_key_down(self, event):
        self.quit(event)
        self.goRight(event)
        self.goLeft(event)
        self.goUp(event)
        self.goDown(event)

    def quit(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def goLeft(self, event, go:bool = True):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = go

    def goRight(self, event, go:bool = True):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = go

    def goUp(self, event, go:bool = True):
        if event.key == pygame.K_UP:
            self.ship.move_up = go

    def goDown(self, event, go:bool = True):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = go
