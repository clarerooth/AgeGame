from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
import re

class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

class AgeGame(BoxLayout):
    pass

class AgeGuessingApp(App):
    q1t = 'How old is Boris Johnson?'
    q2t = 'How old is Jeremy Corbyn?'
    q3t = 'How old is Rupert Murdoch?'
    q4t = 'How old is Number 4?'
    q5t = 'How old is Number 5?'
    q6t = 'How old is Number 6?'


    def build(self):
        self.title='hello clare'
        
        root_widget = AgeGame()
        return root_widget

    def printHello(self, value):
        print('User pressed enter in',value)



if __name__ == "__main__":
  AgeGuessingApp().run()