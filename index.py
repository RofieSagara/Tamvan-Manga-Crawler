from core.mangapark import MangaPark
from holder.chapter import Chapter
from holder.update import Update
from gui.guicreator import GuiCreator
from unicurses import *
import sys

debug = True
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=27, cols=80))


def main():  # {
    mainstdscr = initscr()
    start_color()
    noecho()
    curs_set(False)
    keypad(mainstdscr, True)

    core = MangaPark()
    while True:
        content = core.get_update()
        if content is not None:
            gui = GuiCreator(content)
            break

    while True:  # {
        key = getch()
        if key == KEY_END:
            break
        gui.move(key)
    # }
    endwin()
    return 0
    if debug:
        print("It's Debug!")
        data = Update("Konosuba", None, None, "http://mangapark.me/manga/karneval")
        core = MangaPark()
        di = core.get_info(data)
        dt = Chapter(link="http://mangapark.me/manga/karneval/s3/c1")
        manga = core.get_image(dt)
        del dt
    else:
        core = MangaPark()
        content = core.get_update()
        print("It's Works!")
    return 0
# }


if __name__ == "__main__":  # {
    main()
# }
