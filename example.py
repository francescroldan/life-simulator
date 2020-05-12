import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, SRCALPHA


class Game(object):
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 800
        pygame.display.set_caption("Surfarray test")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill((255, 255, 255))
        self.background.convert()
        self.bar = pygame.Surface((200, 100))
        self.bar.fill((255, 0, 0))
        self.bar.convert()

        self.sprite = pygame.sprite.GroupSingle()
        self.sprite.add(CustomSprite(pygame.Rect(5, 5, 100, 100)))

    def input(self):
        for event in pygame.event.get():

            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
                if event.key == K_SPACE:
                    # make bar transparent by pressing the space bar
                    self.sprite.update()

    def main(self):
        while True:
            if self.input() is False:
                return False
            self.draw()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.bar, (5, 5))
        self.sprite.draw(self.screen)
        pygame.display.update()


class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        # SRCALPHA flag makes the pixel format include per-pixel alpha data
        self.image = pygame.Surface((rect.width, rect.height), SRCALPHA)
        self.image.convert_alpha()
        self.image.fill((126, 126, 126))

    # magic happens here
    def update(self):
        pxa = pygame.surfarray.pixels_alpha(self.image)
        pxa[:] = 100  # make all pixels transparent


if __name__ == "__main__":
    game = Game()
    game.main()
