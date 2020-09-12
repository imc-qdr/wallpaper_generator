from pystray import Icon, Menu, MenuItem
from random import choice
from time import ctime, sleep
import threading
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
run = True


def change_wallpaper():
    path = os.getcwd() + "\\temp.jpg"
    pic = image.get_pic(choice(pics_topics))
    quote_with_pic = image.add_quote(pic, quotes.brainy_quotes_specific(choice(authors)))
    quote_with_pic.save(path, "JPEG")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    print(f'operation successful: {ctime()}')


def create_tray():
    tray = Icon('wisdom on pic', image.Image.open('icon.png'),
                menu=Menu(MenuItem('new image', change_wallpaper),
                          MenuItem('exit', terminate)))
    return tray


def on_schedule():
    while run:
        change_wallpaper()
        sleep(40)
    return


def terminate():
    icon.stop()
    global run
    run = False


if __name__ == '__main__':
    thread = threading.Thread(target=on_schedule)
    thread.start()
    icon = create_tray()
    icon.run()
    thread.join()
