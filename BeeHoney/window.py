import pygame
from obj import Obj
from menu import Menu

class Window:
    def __init__(self, sizex, sizey, title):
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True
        self.fps = pygame.time.Clock()

        self.list_obj = []

    def add_obj(self, item):
        self.list_obj.append(item)

    def draw(self, tela, menu, game,gameover):
        if not menu.change_scene:
            tela.add_obj(menu.bg.draw(tela.window))
        elif gameover.change_scene:
            tela.add_obj(gameover.bg.draw(tela.window))
            game.change_scene = False
        elif menu.change_scene:
            tela.add_obj(game.bg.draw(tela.window))
            tela.add_obj(game.bg2.draw(tela.window))
            tela.add_obj(game.bee.draw(tela.window))
            tela.add_obj(game.spider.draw(tela.window))
            tela.add_obj(game.flower.draw(tela.window))
            tela.add_obj(game.score.draw(tela.window,30,20))
            tela.add_obj(game.life.draw(tela.window, 300, 20))
            game.update(gameover)


    def events(self, menu,game, gameOver):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            elif event.type == pygame.KEYDOWN and gameOver.change_scene:
                if event.key == pygame.K_RETURN:
                    gameOver.events(event)
                    gameOver.change_scene = False
                    menu.change_scene = False
                    game.change_scene = False
                    game.bee.life = 3
                    game.bee.pts = 0
            else:
                menu.events(event)
                game.bee.move_bee(event)

    def update(self, tela, menu, game, gameover):
        while self.loop:
            self.fps.tick(30) # 30 frames por segundo
            self.events(menu, game, gameover)
            self.draw(tela, menu, game, gameover)
            pygame.display.update()


