import arcade

from base.BaseWindow import BaseWindow
from views.MenuView import MenuView


def main():

    window = BaseWindow()
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()