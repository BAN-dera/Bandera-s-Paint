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
		slider_r_control = BanderasPaintApp.slider_color_r.value
		slider_g_control = BanderasPaintApp.slider_color_g.value
		slider_b_control = BanderasPaintApp.slider_color_b.value
		slider_a_control = BanderasPaintApp.slider_color_a.value
		color = (slider_r_control, slider_g_control, slider_b_control, slider_a_control)

		slider_control = BanderasPaintApp.slider.value

		with self.canvas:
			Color(*color)
			rad = slider_control
			window_width, window_height = Window.size
			if touch.y < window_height * 8.5 / 10:
				Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size = (rad, rad))
				touch.ud["line"] = Line(points = (touch.x, touch.y), width = rad / 2)

	def on_touch_move(self, touch):
		window_width, window_height = Window.size
		if touch.y < window_height * 8.5 / 10:
			touch.ud["line"].points += (touch.x, touch.y)

class BanderasPaintApp(App):
	slider_color_r = Slider(value = 0, min = 0, max = 1)
	slider_color_g = Slider(value = 0, min = 0, max = 1)
	slider_color_b = Slider(value = 0, min = 0, max = 1)
	slider_color_a = Slider(value = 0, min = 0, max = 1)
	slider = Slider(value = 8, min = 0, max = 36)
	def build(self):
		# Window layout
		parent = BoxLayout(orientation = "vertical")

		# Layout for buttons
		gl = GridLayout(cols = 6, size_hint = (1, 0.15))

		# Button - Clear and Save
		self.btn_clear = Button(text = "Clear", on_press = self.clear_canvas)
		self.btn_save = Button(text = "Save", on_press = self.save)
		gl.add_widget(self.btn_clear)
		gl.add_widget(self.btn_save)

		# Slider Colors
		bl_colors = BoxLayout(orientation = "vertical")
		bl_colors.add_widget(BanderasPaintApp.slider_color_r)
		bl_colors.add_widget(BanderasPaintApp.slider_color_g)
		bl_colors.add_widget(BanderasPaintApp.slider_color_b)
		bl_colors.add_widget(BanderasPaintApp.slider_color_a)

		gl.add_widget(bl_colors)

		# Slider
		gl.add_widget(BanderasPaintApp.slider)

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
	BanderasPaintApp().run()
