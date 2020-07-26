from .resizer import  image_resize
import random
class Player():
    def __init__(self):
        self.player_width = 30
        self.player_height = 46.5
        self.playerX = 0
        self.playerY = 0
        self.image_dir = 'resources/images/player.png'
    def player_resize(self):
        image_resize(self.image_dir,self.player_width,self.player_height)
    def add_player(self):
        self.playerX = 370
        self.playerY = 480
    def change_position(self,playerX_change):
        self.playerX  += playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >=752:
            self.playerX = 752