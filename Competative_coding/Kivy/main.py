import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# creating the root widget used in .kv file
class RelativeLayout(RelativeLayout):
    pass

# creating the App class in which name
#.kv file is to be named Btn.kv
class BtnApp(App):
    # defining build()
    def build(self):
        # returning the instance of root class
        return RelativeLayout()

# run the app
if __name__ == "__main__":
    BtnApp().run() 
