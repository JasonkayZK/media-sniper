import tkinter as tk

from media_sniper.config import settings


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self._set_window()

    def _set_window(self):
        self.title(settings.APP_NAME)
        scn_width, scn_height = self.maxsize()
        wm_val = "750x450+%d+%d" % ((scn_width - 750) / 2, (scn_height - 450) / 2)
        self.geometry(wm_val)
