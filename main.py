from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Mon App Cameroun 🇨🇲')
        btn = Button(text='Cliquer ici')
        btn.bind(on_press=lambda x: setattr(label, 'text', 'Bonjour!'))
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

MonApp().run()
