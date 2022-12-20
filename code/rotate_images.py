import os
import pathlib
from PIL import Image
 
def rotate_images(directory, rotated_directory):
    if not os.path.exists(rotated_directory):
        os.makedirs(rotated_directory) 
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(path):
            try:
                original_image = Image.open(path)
                rotated_image = original_image.rotate(-90)
                rotated_image = rotated_image.convert('RGB')
                rotated_path = os.path.join(rotated_directory, filename)
                rotated_path = rotated_path.replace(".png", ".jpg")
                rotated_image.save(rotated_path)
                print("saved " + rotated_path + "!")
            except:
                continue

dirname = pathlib.Path(__file__).parent.resolve()
source_dir = os.path.join(dirname, '../images')
rotated_dir = os.path.join(dirname, '../rotated_images')
rotate_images(source_dir, rotated_dir)
