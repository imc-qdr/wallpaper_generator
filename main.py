from threading import Timer
from random import choice
import quotes
import image
import os
import ctypes

pics_topics = ['nature', 'galaxy', 'night sky',
               'peaceful', 'ocean waves', 'cave',
               'forest', 'waterfall', 'aurora']
authors = ['carl-jung', 'alan-watts', 'marcus-aurelius',
           'jordan-peterson', 'terence-mckenna', 'albert-einstein',
           'slavoj-zizek', 'arthur-schopenhauer', 'vincent-van-gogh',
           'lao-tzu', 'oscar-wilde', 'viktor-e-frankl',
           'joseph-campbell', 'lewis-carroll', 'friedrich-nietzsche',
           'mark-twain', 'albert-camus', 'socrates']


def change_wallpaper():
    path = os.getcwd() + "\\temp.jpg"
    pic = image.get_pic(choice(pics_topics))
    quote_with_pic = image.add_quote(pic, quotes.brainy_quotes_specific(choice(authors)))
    quote_with_pic.save(path, "JPEG")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    print("operation successful")
    Timer(40, change_wallpaper).start()


if __name__ == '__main__':
    change_wallpaper()
