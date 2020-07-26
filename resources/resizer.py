from PIL import Image
from resizeimage import resizeimage
  
def image_resize(path,width,height):
    with open(path, 'r+b') as f:
        folder_path = path.split("/")
        folder = ""
        for name in folder_path[0:-1]:
            folder = folder + name +"/"
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [width,height])
            final_path = folder + folder_path[-1][:-4]+"_resized.png"
            cover.save(final_path, image.format)