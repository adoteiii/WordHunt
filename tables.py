from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from arrow import Arrow
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty, ColorProperty, DictProperty, ObjectProperty

from file_tree import resource_path

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard


KV_FILES_DIR = resource_path('kv_files/table_ui.kv')
Builder.load_file(KV_FILES_DIR)


class Block(MDCard):
    text = StringProperty('')
    distance = NumericProperty('20dp')
    color_outer = ColorProperty([0.44, 0.921, 0, 1])
    color_inner = ColorProperty([0, 1, 0, 1])
    text_color = ColorProperty([1, 1, 1, 1])
    arrow_outer_color = ColorProperty([0, 0, 1, 0.05])
    arrow_inner_color = ColorProperty([0.1, 0.2, 1, 1])
    arrow = None
    split = ListProperty([])
    index = ListProperty([])
    root_parent = ObjectProperty(None)

    def __repr__(self):
        return f'Block({self.text}) at position {self.index}'

    def get_direction(self, direction):
        d = ''
        if direction[0] == 1:
            if direction[1] == 0:
                d = 'r'
            elif direction[1] == 1:
                d = 'r-b'
            elif direction[1] == -1:
                d = 'r-t'
        elif direction[0] == -1:
            if direction[1] == 0:
                d = 'l'
            elif direction[1] == 1:
                d = 'l-b'
            elif direction[1] == -1:
                d = 'l-t'
        elif direction[0] == 0:
            if direction[1] == 0:
                d = ''
            elif direction[1] == 1:
                d = 'b'
            elif direction[1] == -1:
                d = 't'
        return d

    def add_arrow(self, direction):
        direction = self.get_direction(direction)
        arrow = None
        if direction:
            split = direction.split('-')
            self.split = split
            x, y, angle = self.get_arrow_pos_angle(self, 0)
            if x is not None and y is not None and angle is not None:
                arrow = Arrow(
                            size_hint=(None, None),
                            size=(0, 0),
                            main_color=self.arrow_inner_color,
                            outline_color=self.arrow_outer_color,
                            o_x=x, 
                            o_y=y,
                            head_size=16,
                            # to_x=random()*self.layout.width,
                            # to_y=random()*self.layout.height,
                            angle=angle,
                            distance=25,
                            fletching_radius=1,
                            distortions=[],
                            head_angle=80
                            )
        if arrow:
            self.arrow = arrow
            self.bind(pos=self.reset_arrow_pos)
            self.reset_arrow_pos(self.pos, (x, y))
            if self.root_parent:
                self.root_parent.ids.arrow_layer.add_widget(self.arrow, canvas='after')
            else:
                self.add_widget(self.arrow, canvas='after')

    def reset_arrow_pos(self, _instance, _value):
        if self.arrow and self.split:
            x, y, angle = self.get_arrow_pos_angle()
            self.arrow.o_x = x
            self.arrow.o_y = y
    
    def get_arrow_pos_angle(self, *_args):
        if self.split:
            x = None
            y = None
            angle = None
            if 'l' in self.split:
                if 'b' in self.split:
                    x = self.x
                    y = self.y
                    angle = 180+45
                elif 't' in self.split:
                    x = self.x
                    y = self.top
                    angle = 90+45
                else:
                    x=self.x
                    y=self.center_y
                    angle=180
            elif 'r' in self.split:
                if 'b' in self.split:
                    x = self.right
                    y = self.y
                    angle = -45
                elif 't' in self.split:
                    x = self.right
                    y = self.top
                    angle = 45
                else:
                    x=self.right 
                    y=self.center_y
                    angle=0
            else:
                if 'b' in self.split:
                    x=self.center_x
                    y=self.y
                    angle=-90
                elif 't' in self.split:
                    x=self.center_x
                    y=self.top
                    angle=90
            return x, y, angle
        return None, None, None


    def remove_arrow(self):
        if self.arrow:
            if self.root_parent:
                self.root_parent.ids.arrow_layer.remove_widget(self.arrow)
            else:
                self.remove_widget(self.arrow)
            self.arrow = None


class Table(MDBoxLayout):
    blocks = DictProperty({})
    word = StringProperty('')
    populated = BooleanProperty(False)
    trace_color = ColorProperty([0, 0, 0, 1])
    trace_points = ListProperty([850, 20, 950, 60])
    inner_color = ColorProperty([0, 1, 0.1, 0.6])
    outer_color = ColorProperty([0, 0, 0, 0])
    block_color = ColorProperty([0, 0, 0, 0])
    text_color = ColorProperty([0, 0, 0, 0])
    row_s = NumericProperty(4)
    cols = NumericProperty(4)
    highlight = ColorProperty([0.8, 0.233, 0.1222, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create)

    def create(self, _dt):
        self._create(self.cols, self.row_s)
        self._fill()

    def _create(self, cols, rows):
        for index_c in range(cols):
            for index_r in range(rows):
                block = Block(text='?', index=[index_r, index_c], root_parent=self)
                self.blocks[(index_r, index_c)] = block

    def _fill(self, *_):
        for block in self.blocks:
            self.ids.grid.add_widget(self.blocks[block])
        if self.word:
            self.populate(self.word)

    def create_point(self, end_r, end_c, start_r=0, start_c=0):
        ids = []
        for index_c in range(start_c, end_c):
            for index_r in range(start_r, end_r):
                ids.append((index_r, index_c))
        return ids
    
    def populate(self, text, send_button=None):
        text = text[:len(self.blocks)]
        self.word = text
        intent = 0
        points = self.create_point(self.row_s, self.cols)
        for index, point in zip(range(len(text)), points):
            self.blocks[point].text = text[index]
            intent += 1
        for index in points[intent:]:
            self.blocks[index].text = '?'
            if send_button:
                send_button.opacity = 0.3
                send_button.disabled = True
            self.populated = False
        if intent >= self.cols*self.row_s:
            if send_button:
                send_button.opacity = 1
                send_button.disabled = False
            self.populated = True

    def get_children_indexes(self, path):
        indexes = []
        for step in path:
            index = step[1]*self.cols + step[0]
            indexes.append(index)
        return indexes

    def add_path(self, path):
        # indexes = self.get_children_indexes(path)
        count = 1
        max_len = len(path)
        self.blocks[tuple(path[0])].md_bg_color = self.highlight
        for index, index_len in zip(path, range(max_len)):
            if count <  max_len:
                self.blocks[tuple(index)].add_arrow([path[index_len+1][0]-path[index_len][0], path[index_len+1][1]-path[index_len][1]])
                count += 1

    def clear_path(self):
        for block in self.blocks:
            self.blocks[block].md_bg_color = MDApp.get_running_app().theme_cls.opposite_bg_dark
            self.blocks[block].remove_arrow()
