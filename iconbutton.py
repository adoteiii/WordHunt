__all__ = ("MIconButton", )


from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, ColorProperty, BooleanProperty, ListProperty
from kivy.animation import Animation
from kivy.uix.togglebutton import ToggleButtonBehavior

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout


Builder.load_string("""
#: import sin math.sin
#: import pi math.pi

<MIconButton>:
    size_hint: None, None
    size: self.user_font_size, self.user_font_size
    # text_color: app.theme_cls.opposite_bg_dark
    rectangle_pos: self.pos[0], self.size[1]
    canvas:
        Color:
            rgba: root.base_color_rectangle
        Rectangle:
            pos: self.pos[0], self.pos[1]
            size: self.size
        Color:
            rgba: root.base_color_circle
        RoundedRectangle:
            pos: self.pos[0]-((self.size[0]**2 + self.size[1]**2)**0.5)*(1 - sin(45)), self.pos[1]-((self.size[0]**2 + self.size[1]**2)**0.5)*(1 - sin(45))
            size: (self.size[0]**2 + self.size[1]**2)**0.5, (self.size[0]**2 + self.size[1]**2)**0.5
            radius: [((self.size[0]**2 + self.size[1]**2)**0.5)/2, ]
        Color:
            rgba: root.base_color_roundedRectangle
        RoundedRectangle:
            pos: self.pos[0]+root.pad_p, self.pos[1]+root.pad_p
            size: self.size[0]-2*root.pad_p, self.size[1]-2*root.pad_p
            radius: root.radius
    MDIcon:
        icon: root.icon
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: root.text_color
        font_size: root.user_font_size*0.5


<ToggleIconButton>:
    size_hint: None, None
    spacing: dp(10)
    size: icon.size[0]+dp(10), icon.size[1]
    text_color: app.theme_cls.bg_light
    icon: 'home'
    base_color: app.theme_cls.bg_normal
    base_color_2: app.theme_cls.bg_dark
    release_button: None
    MDSeparator:
        width: dp(10)
        orientation: 'vertical'
        md_bg_color: root.text_color if root.state == 'down' else root.base_color
    MIconButton: 
        id: icon
        icon: root.icon
        text_color: root.text_color if root.state == 'down' else root.base_color_2
        on_release:
            if callable(root.release_button): root.release_button()
""")


class MIconButton(MDBoxLayout):

    user_font_size = NumericProperty('48sp')

    text_color = ColorProperty([1, 1, 1, 1])

    icon = StringProperty("account-tie")

    disabled_color = ColorProperty([0, 0, 0, 0])

    base_color_rectangle = ColorProperty([0, 0, 0, 0])

    base_color_circle = ColorProperty([0, 0, 0, 0])

    base_color_roundedRectangle = ColorProperty([0, 0, 0, 0])

    rectangle_pos = ListProperty([0, 0])

    rectangle_size = ListProperty([0, 0])

    radius = ListProperty([0, 0, 0, 0])

    pad_p = NumericProperty(0)

    always_release = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_release")
        self.register_event_type("on_press")
        Clock.schedule_once(self.post_init)
    
    def post_init(self, _dt):
        # self.text_color = MDApp.get_running_app().theme_cls.opposite_bg_dark
        pass

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y) and not touch.is_mouse_scrolling and not self.disabled:
            self.schedule_opacity_change_neg()
            self.dispatch("on_press")
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.schedule_opacity_change_pos()
        if self.always_release:
            self.dispatch("on_release")
            return super().on_touch_up(touch)
        if self.collide_point(touch.x, touch.y) and not touch.is_mouse_scrolling and not self.disabled:
            self.dispatch("on_release")
        return super().on_touch_up(touch)
    
    def schedule_opacity_change_neg(self):
        Animation.cancel_all(self, 'opacity')
        animation = Animation(opacity=0.3, duration=0.3)
        animation.start(self)
    
    def schedule_opacity_change_pos(self):
        Animation.cancel_all(self, 'opacity')
        animation = Animation(opacity=1, duration=0.3)
        animation.start(self)

    def on_press(self, *args):
        pass

    def on_release(self, *args):
        pass
    

class ToggleIconButton(MDBoxLayout, ToggleButtonBehavior):
    pass


if __name__ == '__main__':

    class TestApp(MDApp):

        def test(self, *args):
            print(1)
        
        def build(self):
            screen = MDScreen()
            layout = MDFloatLayout()
            button = MIconButton(pos_hint={'center_y': 0.5, 'center_x': 0.5}, base_color_roundedRectangle=[1, 0,1, 1], radius=[15,], pad_p=5)
            button.bind(on_release=self.test)
            layout.add_widget(button)
            screen.add_widget(layout)
            return screen
    
    TestApp().run()