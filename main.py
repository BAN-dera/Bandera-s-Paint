# App running
from kivy.app import App

# Import to create your own widget
from kivy.uix.widget import Widget

# Layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Buttons)
from kivy.uix.button import Button

# Config
from kivy.config import Config

# Input
from kivy.uix.textinput import TextInput

# Slider
from kivy.uix.slider import Slider

# Application window(work with screenshots and saving)
from kivy.core.window import Window

# Draw figures
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class PainterWidget(Widget):
	def on_touch_down(self, touch):
		tit = PaintApp.textinput.text
		if tit.lower() == "grey" or tit.lower() == "серый" or tit.lower() == "color":
			color = (0.33, 0.33, 0.33, 1)
		elif tit.lower() == "red" or tit.lower() == "красный":
			color = (1, 0, 0, 1)
		elif tit.lower() == "green" or tit.lower() == "зелёный" or tit.lower() == "зеленый":
			color = (0, 1, 0, 1)
		elif tit.lower() == "blue" or tit.lower() == "синий":
			color = (0, 0, 1, 1)
		elif tit.lower() == "yellow" or tit.lower() == "жёлтый" or tit.lower() == "желтый":
			color = (1, .84, 0, 1)
		elif tit.lower() == "cyan" or tit.lower() == "бирюзовый":
			color = (0, 1, .88, 1)
		elif tit.lower() == "lightblue" or tit.lower() == "light blue" or tit.lower() == "светлоголубой"or tit.lower() == "светло-голубой" or tit.lower() == "светло голубой":
			color = (0, .35, 1, 1)
		elif tit.lower() == "pink" or tit.lower() == "розовый":
			color = (1, 0, .58, 1)
		elif tit.lower() == "violet" or tit.lower() == "фиолетовый":
			color = (.57, 0, 1, 1)
		elif tit.lower() == "lightviolet" or tit.lower() == "light-violet" or tit.lower() == "light violet" or tit.lower() == "светло фиолетовый" or tit.lower() == "светло-фиолетовый" or tit.lower() == "фиалковый":
			color = (.77, 0, 1, 1)
		elif tit.lower() == "orange" or tit.lower() == "оранжевый":
			color = (1, .42, 0, 1)
		elif tit.lower() == "white" or tit.lower() == "белый":
			color = (1, 1, 1, 1)
		elif tit.lower() == "black" or tit.lower() == "черный" or tit.lower() == "чёрный":
			color = (0, 0, 0, 1)
		else:
			color = (1, 1, 1, 1)

		slider_control = PaintApp.slider.value

		with self.canvas:
			Color(*color)
			rad = slider_control
			window_width, window_height = Window.size
			if touch.y < window_height * 9 / 10:
				Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size = (rad, rad))
				touch.ud["line"] = Line(points = (touch.x, touch.y), width = rad / 2)

	def on_touch_move(self, touch):
		window_width, window_height = Window.size
		if touch.y < window_height * 9 / 10:
			touch.ud["line"].points += (touch.x, touch.y)

class PaintApp(App):
	textinput = TextInput(text = "Color", multiline = False)
	slider = Slider(value = 8, min = 0, max = 36)
	def build(self):
		# Window layout
		parent = BoxLayout(orientation = "vertical")

		# Layout for buttons
		gl = GridLayout(cols = 6, size_hint = (1, 0.1))

		# Button - Clear and Save
		self.btn_clear = Button(text = "Clear", on_press = self.clear_canvas)
		self.btn_save = Button(text = "Save", on_press = self.save)
		gl.add_widget(self.btn_clear)
		gl.add_widget(self.btn_save)

		# Input-Color
		gl.add_widget(PaintApp.textinput)

		# Slider
		gl.add_widget(PaintApp.slider)

		# Layouts for PainterWidget
		bl = BoxLayout()
		self.painter = PainterWidget()
		bl.add_widget(self.painter)

		# Add to window layout
		parent.add_widget(gl)
		parent.add_widget(bl)

		return parent

	def clear_canvas(self, instance):
		self.painter.canvas.clear()

	def save(self, instance):
		self.painter.size = (Window.size[0], Window.size[1])
		self.painter.export_to_png("image.png")

if __name__ == "__main__":
	PaintApp().run()
