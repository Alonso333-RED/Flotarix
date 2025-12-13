from base.BaseView import BaseView
from base.BaseText import BaseText

from config import config


class NewsView(BaseView):
    def __init__(self):
        super().__init__()

        self.title_text = BaseText(
            text="Flotarix",font_size=128,
            x =self.window.width // 2, y=self.window.height * 4 // 5
        )
        self.texts_to_show.append(self.title_text)

        self.author_text = BaseText(
            text="Alonso",font_size=16,
            x =self.window.width // 2, y=self.window.height * 175 // 275
        )
        self.texts_to_show.append(self.author_text)

        self.version_text = BaseText(
            text=config.VERSION,font_size=16,
            x =self.window.width // 2, y=self.window.height * 14 // 24
        )
        self.texts_to_show.append(self.version_text)