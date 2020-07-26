from .resizer import image_resize
class Screen():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.image_dir = 'resources/images/background.png'
    def screen_resize(self):
        image_resize(self.image_dir,self.screen_width,self.screen_height)