from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=20, **kwargs)

        self.add_widget(
            Label(
                text="Voice Assistant 811",
                font_size="28sp"
            )
        )

        self.status = Label(
            text="Project Version 2.0",
            font_size="18sp"
        )

        self.add_widget(self.status)

        btn = Button(
            text="Start Assistant",
            size_hint=(1, None),
            height=55
        )

        btn.bind(on_press=self.start)

        self.add_widget(btn)

    def start(self, instance):
        self.status.text = "Assistant is starting..."


class VoiceAssistantApp(App):

    def build(self):
        self.title = "Voice Assistant 811"
        return MainLayout()


if __name__ == "__main__":
    VoiceAssistantApp().run()
