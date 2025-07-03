from obj import Obj, Bee, Msg
import random

class Game:
    def __init__(self):
        self.bg = Obj("assets/bg.png",0,0)
        self.bg2 = Obj("assets/bg.png", 0, 0)

        self.spider = Obj("assets/spider1.png",random.randrange(0,300),-50)
        self.flower = Obj("assets/flower1.png",random.randrange(0,300),-50)
        self.bee = Bee("assets/bee1.png",150,600)

        self.change_scene = False

        self.score = Msg(60,"0")
        self.life = Msg(60, "3")

    def draw(self, window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.bee.draw(window)
        self.spider.draw(window)
        self.flower.draw(window)
        self.score.draw(window,100,50)
        self.life.draw(window, 200, 50)

    def update(self,gameOver):
        self.move_bg()
        self.spider.anim("spider",8,4)
        self.flower.anim("flower", 8, 2)
        self.bee.anim("bee",2,4)
        self.move_spiders()
        self.move_flower()
        self.bee.colision(self.spider.group,"Spider")
        self.bee.colision(self.flower.group, "Flower")
        self.gameover(gameOver)
        self.score.update_msg(str(self.bee.pts))
        self.life.update_msg(str(self.bee.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] > 630:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0,300), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] > 630:
            self.flower.sprite.kill()
            self.flower = Obj("assets/flower1.png", random.randrange(0,300), -50)

    def gameover(self,gameOver):
        if self.bee.life <= 0:
            self.change_scene = True
            gameOver.change_scene = True

