from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

try:
    from android.permissions import request_permissions, Permission
    HAS_ANDROID = True
except Exception:
    HAS_ANDROID = False

from speech_engine import SpeechEngine
from tts_engine import TTSEngine


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=15, padding=15, **kwargs)

        self.tts = None
        self.speech = None

        self.status = Label(
            text="Voice Assistant 811",
            font_size="22sp"
        )
        self.add_widget(self.status)

        self.result = Label(
            text="Press Start",
            font_size="18sp"
        )
        self.add_widget(self.result)

        self.start_btn = Button(
            text="Start Assistant",
            size_hint=(1, None),
            height=60
        )
        self.start_btn.bind(on_press=self.start_assistant)
        self.add_widget(self.start_btn)

        self.stop_btn = Button(
            text="Stop Assistant",
            size_hint=(1, None),
            height=60
        )
        self.stop_btn.bind(on_press=self.stop_assistant)
        self.add_widget(self.stop_btn)

    def start_assistant(self, *args):

        if HAS_ANDROID:
            request_permissions([Permission.RECORD_AUDIO])

        self.tts = TTSEngine("en_US")
        self.speech = SpeechEngine(
            callback=self.on_result,
            language="en-US"
        )

        Clock.schedule_once(self._start, 1.5)

    def _start(self, dt):

        self.status.text = "Listening..."

        self.tts.speak("Hello. Voice Assistant Eight One One is ready.")

        self.speech.start()

    def stop_assistant(self, *args):

        if self.speech:
            self.speech.stop()

        if self.tts:
            self.tts.stop()

        self.status.text = "Stopped"

    def on_result(self, text):

        Clock.schedule_once(
            lambda dt: self.update_text(text)
        )

    def update_text(self, text):

        self.result.text = text


class VoiceAssistantApp(App):

    def build(self):
        return MainLayout()


VoiceAssistantApp().run()
