__author__ = 'jmeireles'
from gi.repository import Gtk


class Grid():

    widget_list = []
    WIDGET_SIZE = 140
    COLS = 1
    NUM = 100
    grid = ""

    def __init__(self):
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(False)
        grid.set_border_width(0)
        self.grid = grid

    def add_widget(self, widget):
        self.widget_list.append(widget)

    def refresh(self):
        self.remove_widgets()
        self.load_widgets()

    def get(self):
        return self.grid

    def calcule_columns(self, scroll, grid):
        cols = scroll.get_allocated_width() / (self.WIDGET_SIZE + grid.get_column_spacing())
        if cols > len(self.widget_list):
            cols = len(self.widget_list)
        return cols

    def on_resize(self, arg1, arg2, scroll, grid):
        new_cols = self.calcule_columns(scroll, grid)

        if new_cols == self.COLS or new_cols == 0 or new_cols > len(self.widget_list):
            return

        self.COLS = new_cols
        self.remove_widgets()
        self.load_widgets()

    def remove_widgets(self):

        if self.widget_list == 0:
            return

        for wid in self.grid.get_children():
            self.grid.remove(wid)

    def load_widgets(self):
        i,j = 0,0
        COLS = self.COLS

        if len(self.widget_list) == 0: return

        for wid in self.widget_list:
            self.grid.attach(wid, i, j, 1, 1)
            i += 1
            if i == COLS:
                i=0
                j += 1
