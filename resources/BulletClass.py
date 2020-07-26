from .resizer import *

class Bullet():
    def __init__(self):
        self.bullet_width = 24
        self.bullet_height = 24
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_Change = 0
        self.bulletY_Change = 10
        self.state = "ready"
        self.image_dir = 'resources/images/bullet.png'
    def bullet_resize(self):
        image_resize(self.image_dir,self.bullet_width,self.bullet_height)
    def add_bullet(self,X_coordinate,Y_coordinate):
        self.state = "fire"
        self.bulletX = X_coordinate+3
        self.bulletY = Y_coordinate -16
    def fire_bullet(self):
        self.bulletY = self.bulletY - self.bulletY_Change
    def set_instance(self,img):
        self.instance = img

