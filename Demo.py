from holoviews.plotting.bokeh.styles import font_size, color
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)

class MyApp(App):
    def build(self):
        label = Label(text="Hello anupam this is my first app",font_size="100px",bold=True,color=(1,0,0,1))
        return label

MyApp().run()


