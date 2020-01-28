import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Point, GraphicException
from random import random
from math import sqrt


class interfaceApp(App):
    title = 'Trigger Testing Center'

    def build(self):
        return Label()

    def on_pause(self):
        return True

if __name__ == "__main__":
    interfaceApp().run()