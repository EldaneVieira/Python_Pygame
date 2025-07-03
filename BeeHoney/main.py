import pygame.time

from window import Window
from obj import Obj
from menu import Menu, GameOver
from game import Game


class Main:
    def __init__(self):
        self.tela = Window(360,640,"Bee Honey")
        self.start_screen = Obj("assets/start.png", 0, 0)
        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameOver = GameOver("assets/gameover.png")

        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1) #O -1 garante o loop da música de fundo

        
main = Main()
main.tela.update(main.tela, main.menu,main.game, main.gameOver)