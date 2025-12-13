import arcade

from base.BaseWindow import BaseWindow
from views.MenuView import MenuView

def main():

    window = BaseWindow()
    view = MenuView()
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()