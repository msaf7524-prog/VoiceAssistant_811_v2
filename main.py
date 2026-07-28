from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from android.permissions import request_permissions, Permission

from speech_engine import SpeechEngine
from tts_engine import TTSEngine


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)

        self.status = Label(text="Assistant is stopped", font_size="20sp")
        self.add_widget(self.status)

        self.btn_start = Button(text="Start Assistant", size_hint_y=None, height=60)
        self.btn_start.bind(on_press=self.start_assistant)
        self.add_widget(self.btn_start)

        self.btn_stop = Button(text="Stop Assistant", size_hint_y=None, height=60)
        self.btn_stop.bind(on_press=self.stop_assistant)
        self.add_widget(self.btn_stop)

        self.speech_engine = None
        self.tts_engine = None

    def start_assistant(self, instance):
        request_permissions([Permission.RECORD_AUDIO])

        self.tts_engine = TTSEngine(language="en_US")
        self.speech_engine = SpeechEngine(callback=self.on_text, language="en-US")

        try:
            self.speech_engine.start()
            self.status.text = "Listening..."
            if self.tts_engine:
                self.tts_engine.speak("Hello, I am Voice Assistant 811")
        except Exception as e:
            self.status.text = f"Start error: {e}"

    def stop_assistant(self, instance):
        try:
            if self.speech_engine:
                self.speech_engine.stop()
            if self.tts_engine:
                self.tts_engine.stop()
            self.status.text = "Assistant is stopped"
        except Exception as e:
            self.status.text = f"Stop error: {e}"

    def on_text(self, text):
        Clock.schedule_once(lambda dt: self._update_text(text))

    def _update_text(self, text):
        self.status.text = f"Recognized: {text}"


class VoiceAssistantApp(App):
    def build(self):
        self.title = "Voice Assistant 811"
        return MainLayout()


if __name__ == "__main__":
    VoiceAssistantApp().run()
