from .resizer import image_resize
import random
class Enemy():
    def __init__(self):
        self.enemy_width = 48
        self.enemy_height = 48
        self.image_dir = 'resources/images/enemy.png'
        self.enemyX = 0
        self.enemyY = 0
        self.enemyX_Change = 2.5
        self.enemyY_Change = 10
    def enemy_resize(self):
        image_resize(self.image_dir,self.enemy_width,self.enemy_height)
    def add_enemy(self):
        self.enemyX = random.randint(0,751)
        self.enemyY = random.randint(50,150)
    def change_position(self):
        self.enemyX+=self.enemyX_Change
        if self.enemyX<=0:
            self.enemyX_Change = 2.5
            self.enemyY +=  self.enemyY_Change
        elif self.enemyX>=752:
            self.enemyX_Change = -2.5
            self.enemyY += self.enemyY_Change
    def set_instance(self,img):
            self.instance = img
    def add_bullet(self,bullet):
        self.bullet = bullet
class enemyBullet():
    def __init__(self):
        self.width = 24
        self.height = 24
        self.X = 0
        self.Y = 0
        self.Y_Change = 3.5
        self.X_Change = 0
        self.state = "ready"
        self.image_dir = 'resources/images/fireball.png'
    def resize(self):
        image_resize(self.image_dir,self.width,self.height)
    def add_bullet(self,X_coordinate,Y_coordinate):
        self.state = "fire"
        self.X = X_coordinate+8
        self.Y = Y_coordinate +16
    def fire_bullet(self):
        self.Y = self.Y + self.Y_Change
    def set_instance(self,img):
        self.instance = img