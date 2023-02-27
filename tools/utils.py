import os

from PIL import Image


def create_animation(images_path, animation_path, duration=100, loop=0):
    files = sorted(os.listdir(images_path))
    choose_only_png = [os.path.join(images_path, f) for f in files if f.endswith('.png')]

    with Image.open(choose_only_png[0]) as im:
        im.save(animation_path, save_all=True, append_images=[Image.open(picture) for picture in choose_only_png[1:]],
                duration=duration, loop=loop)


def run(PATH_TO_IMG):
    animation_path = f"{PATH_TO_IMG}\\testing_adding_goods_to_cart_animation.gif"
    create_animation(PATH_TO_IMG, animation_path, duration=1000, loop=0)
