
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from tables import Block
from arrow import Arrow
from kivymd.app import MDApp
from tables import Table

class WordGame(MDApp):
    resource_path = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.table = Block(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # self.table.add_path([[0, 0], [0, 1], [0, 2], [1, 1], [2, 2]])
        # self.table.add_arrow([1, -1])
        # self.table.add_arrow([1, 0])
        # self.table.add_arrow([1, 1])
        # self.table.add_arrow([0, -1])
        # self.table.add_arrow([0, 1])
        # # self.table.add_arrow([0, -1])
        # self.table.add_arrow([-1, -1])
        # self.table.add_arrow([-1, 0])
        self.table.add_arrow([-1, 1])
        print(self.table.pos)
        return self.table


if __name__ == '__main__':
    app = WordGame()
    app.run()