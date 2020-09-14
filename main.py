from pystray import Icon, Menu, MenuItem
from random import choice
from time import ctime, sleep
from threading import Thread
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
    pic = image.get_pic(choice(pics_topics))
    quote_with_pic = image.add_quote(pic, quotes.brainy_quotes_specific(choice(authors)))
    quote_with_pic.save(r'files\temp.jpg', "JPEG")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+r'\files\temp.jpg', 0)
    print(f'operation successful: {ctime()}')


def create_tray():
    global pause_state
    pause_state = False
    pause = MenuItem('pause', lambda: option('pause'), checked=lambda state: pause_state)
    tray = Icon('wisdom on pic', title='Wallpaper Wisdom', icon=image.Image.open(r'files\icon.png'),
                menu=Menu(MenuItem('new image', change_wallpaper),
                          pause,
                          MenuItem('exit', lambda: option('exit'))))
    return tray


def on_schedule():
    while run:
        change_wallpaper()
        sleep(30)
    return


def option(string):
    global pause_state, run
    if string == 'exit':
        run = False
        icon.stop()
    else:
        if not pause_state:
            run, pause_state = False, True
        else:
            run, pause_state = True, False
            Thread(target=on_schedule).start()


if __name__ == '__main__':
    Thread(target=on_schedule).start()
    icon = create_tray()
    icon.update_menu()
    icon.run()
