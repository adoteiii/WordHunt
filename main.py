# kivy imports
from kivy.properties import StringProperty, ListProperty, ObjectProperty, BooleanProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivy.core.window import Window

# kivymd imports
from kivymd.app import MDApp
from kivymd.effects.stiffscroll import StiffScrollEffect
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard

# other module imports
from iconbutton import MIconButton
from tables import Table
from file_tree import resource_path
from cardtextinput import M_CardTextField

# wordhunt imports
from wordhuntanagram.anagram import Anagram
from wordhuntanagram.wordhunt import WordHunt
# from wordhuntanagram.base import WORDS_TRIE

Builder.load_string(
"""


<Manager>:
    MainScreen:
        id: mainscreen


<MainScreen>:
    name: 'mainscreen'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal
        MDBoxLayout:
            MDBoxLayout:
                id: ribbon
                size_hint_x: None
                width: dp(48)
                spacing: dp(10)
                padding: dp(0), dp(10), dp(0), dp(10)
                orientation: 'vertical'
                md_bg_color: [0.08923, 0.09, 0.08, 0.7]
                AnchorLayout:
                    size_hint_y: None
                    height: home_icon.height
                    MIconButton:
                        id: home_icon
                        icon: 'home'
                        size: dp(30), dp(30)
                        text_color: [1, 1, 1, 1]
                AnchorLayout:
                    size_hint_y: None
                    height: home_icon.height
                    MIconButton:
                        icon: 'new-box'
                        text_color: [1, 1, 1, 1]
                        size: dp(30), dp(30)
                        on_release:
                            root.clear()
                MDBoxLayout:
                AnchorLayout:
                    size_hint_y: None
                    height: home_icon.height
                    MIconButton:
                        icon: 'cog'
                        size: dp(30), dp(30)
                        text_color: [1, 1, 1, 1]
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                md_bg_color: app.theme_cls.bg_normal
                MDBoxLayout:
                    padding: dp(0), dp(0), dp(0), dp(0)
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    spacing: dp(0)
                    MDBoxLayout:
                        padding: dp(0), dp(0), dp(10), dp(0)
                        size_hint_y: None
                        height: self.minimum_height
                        md_bg_color: app.theme_cls.bg_dark
                        spacing: dp(0)
                        MDBoxLayout:
                        MDBoxLayout:
                            size_hint: None, None
                            size: dp(20), dp(23)
                            MDLabel:
                                text: 'C:'
                                font_size: sp(12)
                                font_style: 'Overline'
                                halign: 'center'
                        MDBoxLayout:
                            size_hint: None, None
                            size: dp(20), dp(23)
                            md_bg_color: app.theme_cls.accent_color
                            CustomTextInput:
                                id: column_textfield
                                size_hint_x: None
                                width: dp(20)
                                font_size: sp(12)
                                size_hint_y: None
                                height: dp(24)
                                text: str(main_table.cols)
                                background_color: [0, 0, 0, 0]
                                border: [4, 4, 4, 4]
                                cursor_color: app.theme_cls.opposite_bg_light
                                foreground_color: app.theme_cls.opposite_bg_light
                                disabled_foreground_color: [0, 0, 0, 0]
                                max_chars: 1
                                input_filter: 'int'
                            Widget:
                        MDBoxLayout:
                            size_hint: None, None
                            size: dp(20), dp(23)
                            MDLabel:
                                text: 'R:'
                                font_size: sp(12)
                                font_style: 'Overline'
                                halign: 'center'
                        MDBoxLayout:
                            size_hint: None, None
                            size: dp(20), dp(23)
                            md_bg_color: app.theme_cls.accent_color
                            CustomTextInput:
                                id: row_textfield
                                size_hint_x: None
                                width: dp(20)
                                font_size: sp(12)
                                size_hint_y: None
                                height: dp(24)
                                text: str(main_table.row_s)
                                background_color: [0, 0, 0, 0]
                                border: [4, 4, 4, 4]
                                cursor_color: app.theme_cls.opposite_bg_light
                                foreground_color: app.theme_cls.opposite_bg_light
                                disabled_foreground_color: [0, 0, 0, 0]
                                max_chars: 1
                                input_filter: 'int'
                            Widget:
                    MDSeparator:
                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(0), dp(20), dp(0), dp(0)
                        md_bg_color: app.theme_cls.bg_normal
                        Widget:
                        Table:
                            id: main_table
                            row_s: 4
                            inner_color: app.theme_cls.primary_color
                        Widget:
                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(10), dp(10), dp(10), dp(10)
                        size_hint_min_x: dp(300)
                        spacing: dp(20)
                        M_CardTextField:
                            id: field
                            # icon_left: 'magnify'
                            grow: False
                            hint_text: 'Type in letters'
                            filter_input: 'alpha'
                            max_chars: 16
                            on_valid_text:
                                main_table.populate(self.valid_text, send_button)
                        MDBoxLayout:
                            padding: dp(0), dp(0 ), dp(10), dp(0)
                            size_hint: None, 1
                            size: send_button.size
                            md_bg_color: app.theme_cls.bg_normal
                            AnchorLayout:
                                anchor_x: 'right'
                                MIconButton:
                                    id: send_button
                                    # base_color_circle: app.theme_cls.primary_color
                                    text_color: app.theme_cls.primary_color
                                    icon: 'send'
                                    size: dp(30), dp(30)
                                    # user_font_size: sp(30)
                                    # size: dp(24), dp(24)
                                    opacity: 0.3
                                    disabled: True
                                    on_release:
                                        root.add_table(main_table)
                                        self.disabled = True
                                        field.disabled = True
                MDCard:
                    radius: dp(0), dp(0), dp(0), dp(0)
                    padding: dp(10)
                    # Recycleview
                    spacing: dp(25)
                    Widget:
                    MDBoxLayout:
                        padding: dp(0)
                        orientation: 'vertical'
                        size_hint_x: None
                        width: solution_table.width
                        Table:
                            id: solution_table
                            row_s: 4
                        Widget:
                    Widget:
                            
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(40)
                    padding: dp(20), dp(0), dp(20), dp(10)
                    AnchorLayout:
                        size_hint_x: None
                        width: icon_box.width
                        MDBoxLayout:
                            id: icon_box
                            size_hint: None, None
                            size: dp(30), dp(30)
                            MIconButton:
                                icon: 'arrow-left'
                                size: dp(30), dp(30)
                                text_color: app.theme_cls.primary_color
                                on_release:
                                    root.prev_item()
                    MDLabel:
                        id: word_label
                        text: ""
                        halign: 'center'
                    AnchorLayout:
                        size_hint_x: None
                        width: icon_box.width
                        MDBoxLayout:
                            size_hint: None, None
                            size: dp(30), dp(30)
                            MIconButton:
                                icon: 'arrow-right'
                                size: dp(30), dp(30)
                                text_color: app.theme_cls.primary_color
                                on_release:
                                    root.next_item()
                    
        MDBoxLayout:
            size_hint_y: None
            height: dp(24)
            md_bg_color: app.theme_cls.primary_color


<Row>:
    md_bg_color: app.theme_cls.primary_color
    # elevation: 0
    radius: [dp(10), dp(10), dp(10), dp(10)]
    padding: dp(0), dp(0), dp(0), dp(0)
    value: ''
    Label:
        id: name
        # color: app.theme_cls.opposite_bg_dark
        halign: 'center'
        bold: True
        font_size: sp(14)
    Label:
        size_hint_x: None
        width: dp(0)
        text: root.value
        # color: app.theme_cls.opposite_bg_dark
"""
)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class Row(RecycleKVIDsDataViewBehavior, MDCard):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(Row, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(Row, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            self.md_bg_color = MDApp().get_running_app().theme_cls.accent_color
        else:
            self.md_bg_color = MDApp().get_running_app().theme_cls.primary_color

class MainScreen(MDScreen):

    data = ListProperty([])
    index = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self.keys_init, self)
        self._keyboard.bind(on_key_down=self.keyboard_motion)

    def keys_init(self, *args):
        print(args)

    def keyboard_motion(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.prev_item()
        if keycode[1] == 'right':
            self.next_item()
    
    def add_table(self, table):
        word_hunt = WordHunt(table.cols, table.row_s, args=table.word, auto_input=False)
        word_hunt.hunt()
        self.ids.solution_table.populate(table.word, None)
        self.populate(word_hunt)

    def populate(self, data):
        self.data = [{'word': str(x), 'path': data.words[x]} for x in data.words]
        self.sort()
        if self.data:
            self.set_text(self.data[0]['word'])
            self.set_table(self.data[0]['path'])

    def set_table(self, path):
        self.clear_table()
        self.ids.solution_table.add_path(path)

    def clear_table(self):
        self.ids.solution_table.clear_path()

    def set_text(self, word):
        self.ids.word_label.text = word

    def sort(self):
        self.data = sorted(self.data, key=lambda x: len(x['word']), reverse=True)

    def clear(self):
        self.data = []
        self.ids.field.disabled = False
        self.clear_table()
        self.set_text('')
        self.ids.field.ids.textfield.text = ''
        self.index = 0
        # self.ids.field.base_color_circle = MDApp.get_running_app().theme_cls.primary_color

    def next_item(self):
        print(self.data[self.index+1]['word'])
        if self.index+1 < len(self.data):
            self.set_text(self.data[self.index+1]['word'])
            self.set_table(self.data[self.index+1]['path'])
            self.index += 1

    def prev_item(self):
        if self.index-1 >= 0:
            self.set_text(self.data[self.index-1]['word'])
            self.set_table(self.data[self.index-1]['path'])
            self.index -= 1

    def remove(self):
        if self.data:
            self.data.pop(0)


class Manager(ScreenManager):
    pass


class WordGame(MDApp):
    resource_path = None

    def __init__(self, **kwargs):
        self.resource_path = resource_path
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.manager = Manager()
        return self.manager


if __name__ == '__main__':
    app = WordGame()
    app.run()