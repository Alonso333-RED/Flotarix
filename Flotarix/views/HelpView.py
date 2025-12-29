import arcade
import arcade.gui
from base.BaseView import BaseView
from base.BaseText import BaseText
from base.BaseLargeText import BaseLargeText
from base.BaseButton import BaseButton
from utils import assets_utils
from config import config

class HelpView(BaseView):
    def __init__(self):
        super().__init__()

        self.title_text = BaseText(text="Flotarix",font_size=128)
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(text="Alonso",font_size=16)
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(text=config.VERSION,font_size=16)
        self.texts_to_show.append(self.version_text)

        self.help_text = """Flotarix
Juego de estrategia por turnos para 2 a 4 jugadores, inspirado en el ajedrez. Cada jugador controla una flota de naves espaciales sobre un tablero, y en cada turno solo puede realizar una acción, por lo que cada decisión importa.

Objetivo
Elimina a todos los oponentes y sé el último en pie. Debilitar progresivamente la flota enemiga es clave para alcanzar la victoria.

Naves y Combate
Cada nave posee un patrón de ataque distinto, con diferentes alcances y formas. Para atacar, debes posicionar una nave de modo que una nave enemiga coincida con una de sus casillas atacables. Las naves bajo ataque pierden integridad por turno según el daño recibido, hasta ser destruidas o retiradas a una casilla segura. Atacar múltiples objetivos y evitar quedar expuesto es parte fundamental de la estrategia.

Nave Insignia y Energía
Cada jugador cuenta con una Nave Insignia, única e irremplazable, que permite generar nuevas naves. Si es destruida, ya no podrás crear refuerzos, quedando en gran desventaja. Crear naves consume energía, el recurso principal para expandir tu flota, por lo que administrarla y proteger tus naves clave es esencial.

Controles
Selecciona una nave con el cursor para moverla o usar su función. Para generar nuevas naves, haz clic sobre la Nave Insignia o una nave con capacidad de creación, elige la nave deseada y paga su costo de energía."""

        self.text_space = BaseLargeText(self.help_text, 
                                        width=self.window.width * 0.75,
                                        height=self.window.height * 0.33,
                                        font_size=18)

        self.uimanager.add(self.text_space)

        self.back_button = BaseButton("Atras", width = config.WINDOW_WIDTH * 0.25, when_clicked=self.on_click_back)
        self.prepare_button(self.back_button)

    def update_layout(self):

        self.title_text.x = self.window.width * 0.5
        self.title_text.y = self.window.height * 0.8

        self.author_text.x = self.window.width * 0.5
        self.author_text.y = self.window.height * 0.64

        self.version_text.x = self.window.width * 0.5
        self.version_text.y = self.window.height * 0.6

        self.text_space.center_x = self.window.width * 0.5
        self.text_space.center_y = self.window.height * 0.4125

        self.back_button.center_x = self.window.width * 0.5
        self.back_button.center_y = self.window.height * 0.2
    
    def on_draw(self):
        super().on_draw()

    def on_resize(self, width, height):
        super().on_resize(width, height)

    def on_show_view(self):
        super().on_show_view()

    def on_click_back(self, event: arcade.gui.UIOnClickEvent):
        print("back clicked.")
        assets_utils.execute_sound("click.mp3", self.ui_volume)
        from views.MenuView import MenuView
        self.uimanager.clear()
        view = MenuView()
        self.window.show_view(view)