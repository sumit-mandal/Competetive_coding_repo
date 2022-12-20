import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('main.kv')

class Shot(Widget):

	# Method to disable one button and activate the other.
	def disable_other(self):
		if self.ids.but_two.disabled == False:
			self.ids.but_two.disabled = True
			self.ids.but_one.disabled = False
			# Add some color to make it more visual for which one is active.
			self.ids.but_one.background_color = (0,0,1,1)
			self.ids.but_one.color = (1,1,1,1)

			self.ids.but_two.background_color = (0,0,0,1)
			self.ids.but_two.color = (0,0,0,1)
			print('Button One is now disabled. Button Two is now enabled.')
		else:
			self.ids.but_one.disabled = True
			self.ids.but_two.disabled = False
			# Add some color to make it more visual for which one is active.
			self.ids.but_two.background_color = (0,0,1,1)
			self.ids.but_two.color = (1,1,1,1)

			self.ids.but_one.background_color = (0,0,0,1)
			self.ids.but_one.color = (0,0,0,1)
			print('Button One is now enabled. Button Two is now disabled.')

class ShotApp(App):
	def build(self):
		return Shot()

if __name__ == '__main__':
	ShotApp().run()
