from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
class M(App):
    def build(self):
        la = BoxLayout(padding=10, orientation='vertical')
        b = Button(text='Сложить')
        b.bind(on_press=self.on_p)
        self.l = Label(text='')
        self.t1 = TextInput()
        self.t2 = TextInput()
        la.add_widget(self.t1)
        la.add_widget(self.t2)
        la.add_widget(b)
        la.add_widget(self.l)
        return la
    def on_p(self, instance):
        self.l.text = str(int(self.t1.text) + int(self.t2.text))
app = M()
app.run()
