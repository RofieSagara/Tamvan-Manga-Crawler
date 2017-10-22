from unicurses import *

from core.mangapark import MangaPark
from holder.update import Update


class GuiCreator:  # {
    window_header = None
    panel_header = None
    window_body = None
    panel_body = None
    window_bottom = None
    panel_bottom = None
    panel_mini_0 = None
    panel_mini_1 = None
    panel_mini_2 = None
    panel_mini_3 = None
    panel_mini_4 = None
    panel_mini_5 = None
    panel_mini_6 = None
    panel_mini_7 = None
    panel_mini_8 = None
    panel_info = None
    panel_info_browser = None
    panel_info_chapter = None
    panel_info_close = None
    lupdate = None
    lshow = None
    page = None
    select_index = None
    info_status = True
    info_chapter = False
    control_info_select = 2
    position_summary = 5
    all_position_summary = 0
    data_manga_info = None

    def __init__(self, update=None):  # {
        self.lshow = []
        self.select_index = 0
        self.page = 0
        self.lupdate = update
        self.set_data()
        self.create_header()
        self.create_body()
        self.create_bottom()
        self.refresh()
    # }

    def set_data(self):  # {
        self.lshow.clear()
        m = self.page-1
        for n in range(m, m+9):
            self.lshow.append(self.lupdate[n])
        self.page += 9
    # }

    def move(self, key):  # {
        if key == KEY_UP:  # {
            if self.info_status:
                if self.select_index != 0 and self.select_index != 3 and self.select_index != 6:
                    self.select_index -= 1
                    self.create_body()
            elif not self.info_status:
                if self.position_summary > 5 and self.all_position_summary > 5:
                    self.position_summary -= 1
                    self.create_pop()
        # }
        elif key == KEY_DOWN:  # {
            if self.info_status:
                if self.select_index != 2 and self.select_index != 5 and self.select_index != 8:
                    self.select_index += 1
                    self.create_body()
            elif not self.info_status:
                if self.position_summary != self.all_position_summary and self.all_position_summary > 5:
                    self.position_summary += 1
                    self.create_pop()
        # }
        elif key == KEY_LEFT:  # {
            if self.info_status:
                if self.select_index != 0 and self.select_index != 1 and self.select_index != 2:
                    self.select_index -= 3
                    self.create_body()
            elif not self.info_status:
                if self.control_info_select != 0:
                    self.control_info_select -= 1
                    self.create_pop_control()
        # }
        elif key == KEY_RIGHT:  # {
            if self.info_status:
                if self.select_index != 6 and self.select_index != 7 and self.select_index != 8:
                    self.select_index += 3
                    self.create_body()
            elif not self.info_status:
                if self.control_info_select != 2:
                    self.control_info_select += 1
                    self.create_pop_control()
        # }
        elif key == 44 or key == 339:  # {
            if self.page > 17:
                self.page -= 18
                self.set_data()
                self.create_body()
        # }
        elif key == 46 or key == 338:  # {
            if not (self.page + 8) >= len(self.lupdate):
                self.set_data()
                self.create_body()
        # }
        elif key == 10:  # {
            if self.info_status and not self.info_chapter:
                self.info_status = False
                self.data_manga_info = None
                self.position_summary = 5
                self.create_pop()
            elif not self.info_status and not self.info_chapter:
                if self.control_info_select == 2:
                    hide_panel(self.panel_info)
                    hide_panel(self.panel_info_close)
                    hide_panel(self.panel_info_chapter)
                    hide_panel(self.panel_info_browser)
                    self.info_status = True
                    self.create_body()
                elif self.control_info_select == 0:
                    hide_panel(self.panel_info)
                    hide_panel(self.panel_info_close)
                    hide_panel(self.panel_info_chapter)
                    hide_panel(self.panel_info_browser)
                    self.info_status = True
                    self.info_chapter = True
                    self.create_body()
        # }
        wmove(self.window_bottom, 1, 1)
        waddstr(self.window_bottom, "Position Summary :"+str(self.position_summary))
        self.refresh()
    # }

    def create_header(self):  # {
        self.window_header = newwin(4, 80, 0, 0)
        box(self.window_header)
        wmove(self.window_header, 1, 29)
        waddstr(self.window_header, "Tamvan Manga Downloader")
        wmove(self.window_header, 2, 35)
        waddstr(self.window_header, "Version 1.0")

        self.panel_header = new_panel(self.window_header)
        move_panel(self.panel_header, 0, 0)
    # }

    def create_body(self):  # {
        self.window_body = newwin(20, 80, 4, 0)
        box(self.window_body)
        wmove(self.window_body, 0, 1)
        waddstr(self.window_body, "Last Update")
        self.panel_body = new_panel(self.window_body)
        move_panel(self.panel_body, 4, 0)

        if self.info_status and not self.info_chapter:
            self.create_update_body()
        elif self.info_status and self.info_chapter:
            self.create_chapter_body()
    # }

    def create_chapter_body(self):  #{
        win = self.create_mini_chapter(0)
        self.panel_mini_0 = new_panel(win)
        move_panel(self.panel_mini_0, 5, 1)
        del win

        win = self.create_mini_chapter(1)
        self.panel_mini_1 = new_panel(win)
        move_panel(self.panel_mini_1, 6, 1)
        del win

        win = self.create_mini_chapter(2)
        self.panel_mini_2 = new_panel(win)
        move_panel(self.panel_mini_2, 7, 1)
        del win

        win = self.create_mini_chapter(3)
        self.panel_mini_3 = new_panel(win)
        move_panel(self.panel_mini_3, 8, 1)
        del win

        win = self.create_mini_chapter(4)
        self.panel_mini_4 = new_panel(win)
        move_panel(self.panel_mini_4, 9, 1)
        del win

        win = self.create_mini_chapter(5)
        self.panel_mini_5 = new_panel(win)
        move_panel(self.panel_mini_5, 10, 1)
        del win

        win = self.create_mini_chapter(6)
        self.panel_mini_6 = new_panel(win)
        move_panel(self.panel_mini_6, 11, 1)
        del win

        win = self.create_mini_chapter(7)
        self.panel_mini_7 = new_panel(win)
        move_panel(self.panel_mini_7, 12, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_8 = new_panel(win)
        move_panel(self.panel_mini_8, 13, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_9 = new_panel(win)
        move_panel(self.panel_mini_9, 14, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_10 = new_panel(win)
        move_panel(self.panel_mini_10, 15, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_11 = new_panel(win)
        move_panel(self.panel_mini_11, 16, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_12 = new_panel(win)
        move_panel(self.panel_mini_12, 17, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_13 = new_panel(win)
        move_panel(self.panel_mini_13, 18, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_14 = new_panel(win)
        move_panel(self.panel_mini_14, 19, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_15 = new_panel(win)
        move_panel(self.panel_mini_15, 20, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_16 = new_panel(win)
        move_panel(self.panel_mini_16, 21, 1)
        del win

        win = self.create_mini_chapter(8)
        self.panel_mini_17 = new_panel(win)
        move_panel(self.panel_mini_17, 22, 1)
        del win
    # }

    def create_update_body(self):  #{
        win = self.create_mini_update(0)
        self.panel_mini_0 = new_panel(win)
        move_panel(self.panel_mini_0, 5, 1)
        del win

        win = self.create_mini_update(1)
        self.panel_mini_1 = new_panel(win)
        move_panel(self.panel_mini_1, 11, 1)
        del win

        win = self.create_mini_update(2)
        self.panel_mini_2 = new_panel(win)
        move_panel(self.panel_mini_2, 17, 1)
        del win

        win = self.create_mini_update(3)
        self.panel_mini_3 = new_panel(win)
        move_panel(self.panel_mini_3, 5, 27)
        del win

        win = self.create_mini_update(4)
        self.panel_mini_4 = new_panel(win)
        move_panel(self.panel_mini_4, 11, 27)
        del win

        win = self.create_mini_update(5)
        self.panel_mini_5 = new_panel(win)
        move_panel(self.panel_mini_5, 17, 27)
        del win

        win = self.create_mini_update(6)
        self.panel_mini_6 = new_panel(win)
        move_panel(self.panel_mini_6, 5, 53)

        win = self.create_mini_update(7)
        self.panel_mini_7 = new_panel(win)
        move_panel(self.panel_mini_7, 11, 53)
        del win

        win = self.create_mini_update(8)
        self.panel_mini_8 = new_panel(win)
        move_panel(self.panel_mini_8, 17, 53)
        del win
    # }

    def create_mini_chapter(self, idx=None):  #{
        window_mini = newwin(1, 78, 0, 0)
        box(window_mini)
        wmove(window_mini, 0, 0)
        waddstr(window_mini, "Chapter 12")

        idy = 2
        if idx == self.select_index:  # {
            wbkgd(window_mini, A_REVERSE)
        # }
        return window_mini
    # }

    def create_mini_update(self, idx=None):  #{
        window_mini = newwin(6, 25, 0, 0)
        box(window_mini)
        wmove(window_mini, 1, 1)
        waddstr(window_mini, self.lshow[idx].title[0:23])

        idy = 2
        for n in self.lshow[idx].update_chapter:
            wmove(window_mini, idy, 1)
            waddstr(window_mini, n.title[0:23])
            idy += 1
        if idx == self.select_index:  # {
            wbkgd(window_mini, A_REVERSE)
        # }
        return window_mini
    # }

    def create_pop(self):  # {
        dt = self.lshow[self.select_index]
        if self.data_manga_info is None:
            core = MangaPark()
            while True:
                info = core.get_info(dt)
                if info is not None:
                    self.data_manga_info = info
                    break
        win = self.create_pop_info(self.data_manga_info)
        self.panel_info = new_panel(win)
        move_panel(self.panel_info, 3, 5)
        show_panel(self.panel_info)
        del win
        self.create_pop_control()
    # }

    def create_pop_control(self):  # {
        win = self.create_pop_button("Open Browser", 0)
        self.panel_info_browser = new_panel(win)
        move_panel(self.panel_info_browser, 21, 7)
        del win

        win = self.create_pop_button("Show Chapter", 1)
        self.panel_info_chapter = new_panel(win)
        move_panel(self.panel_info_chapter, 21, 34)
        del win

        win = self.create_pop_button("Close", 2)
        self.panel_info_close = new_panel(win)
        move_panel(self.panel_info_close, 21, 63)
        del win
    # }

    def create_pop_button(self, text, indx):  # {
        window_mini = None
        if text == "Open Browser":
            window_mini = newwin(1, 16, 0, 0)
        elif text == "Show Chapter":
            window_mini = newwin(1, 16, 0, 0)
        elif text == "Close":
            window_mini = newwin(1, 9, 0, 0)

        if self.control_info_select == indx:
            wmove(window_mini, 0, 1)
            waddstr(window_mini, "="+text+"=")
        else:
            wmove(window_mini, 0, 2)
            waddstr(window_mini, text)

        return window_mini
    # }

    def create_pop_info(self, info):  # {
        window_mini = newwin(21, 70, 0, 0)
        box(window_mini)
        wmove(window_mini, 1, 30)
        waddstr(window_mini, "Info Manga")
        wmove(window_mini, 2, 1)
        waddstr(window_mini, info.title)
        wmove(window_mini, 3, 1)
        waddstr(window_mini, "Rating   :"+info.rating)
        wmove(window_mini, 4, 1)
        waddstr(window_mini, "Rank     :"+info.rank)
        wmove(window_mini, 5, 1)
        waddstr(window_mini, "Alt      :"+info.alternative[0:38])
        wmove(window_mini, 6, 1)
        waddstr(window_mini, "Author(s):"+info.author[0:55])
        wmove(window_mini, 7, 1)
        waddstr(window_mini, "Artist(s):"+info.artist[0:55])
        wmove(window_mini, 8, 1)
        waddstr(window_mini, "Genre(s) :"+info.genre[0:55])
        wmove(window_mini, 9, 1)
        waddstr(window_mini, "Type     :"+info.typemanga)
        wmove(window_mini, 10, 1)
        waddstr(window_mini, "Release  :"+info.release)
        wmove(window_mini, 11, 1)
        waddstr(window_mini, "Status   :"+info.status)
        lsummary = []

        text = ""
        for x in range(len(info.summary)):
            ttext = text
            ttext = ttext + info.summary[x]
            if not len(ttext) == 68:
                text = ttext
            else:
                if text[66] == " ":
                    lsummary.append(text)
                elif text[0] == " ":
                    text = text[1:]
                    lsummary.append(text)
                else:
                    text = text+"-"
                    lsummary.append(text)
                text = info.summary[x]
        lsummary.append(text)
        self.all_position_summary = len(lsummary)
        i = 12
        self.position_summary -= 5
        if self.all_position_summary < 5:
            m = self.all_position_summary-1
        else:
            m = 5
        for n in range(m):
            wmove(window_mini, i, 1)
            waddstr(window_mini, lsummary[self.position_summary])
            i += 1
            self.position_summary += 1
        wbkgd(window_mini, A_REVERSE)
        return window_mini
    # }

    def create_bottom(self):  # {
        self.window_bottom = newwin(3, 80, 21, 0)
        box(self.window_bottom)
        wmove(self.window_bottom, 0, 1)
        waddstr(self.window_bottom, "Control")
        self.panel_bottom = new_panel(self.window_bottom)
        move_panel(self.panel_bottom, 24, 0)

    def refresh(self):  # {
        update_panels()
        doupdate()
    # }

# }
