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

        self.speech = None
        self.tts = None
        self.is_running = False

        self.title_label = Label(
            text="Voice Assistant 811",
            font_size="24sp"
        )
        self.add_widget(self.title_label)

        self.status = Label(
            text="Press Start",
            font_size="18sp"
        )
        self.add_widget(self.status)

        self.result = Label(
            text="No speech yet",
            font_size="16sp"
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
        if self.is_running:
            return

        if HAS_ANDROID:
            try:
                request_permissions([Permission.RECORD_AUDIO])
            except Exception as e:
                self.status.text = f"Permission error: {e}"
                return

        try:
            if self.tts is None:
                self.tts = TTSEngine(language="en_US")

            if self.speech is None:
                self.speech = SpeechEngine(
                    callback=self.on_text,
                    language="en-US"
                )

            self.status.text = "Starting..."
            self.is_running = True

            Clock.schedule_once(self._start_session, 1.5)

        except Exception as e:
            self.is_running = False
            self.status.text = f"Start error: {e}"

    def _start_session(self, dt):
        if not self.is_running:
            return

        try:
            if self.tts:
                self.tts.speak("Hello, I am Voice Assistant 811")
        except Exception:
            pass

        try:
            if self.speech:
                self.speech.start()
                self.status.text = "Listening..."
        except Exception as e:
            self.status.text = f"Speech start error: {e}"
            self.is_running = False

    def stop_assistant(self, *args):
        self.is_running = False

        try:
            if self.speech:
                self.speech.stop()
        except Exception:
            pass

        try:
            if self.tts:
                self.tts.stop()
                self.tts.shutdown()
        except Exception:
            pass

        self.status.text = "Stopped"

    def on_text(self, text):
        Clock.schedule_once(lambda dt: self._update_text(text))

    def _update_text(self, text):
        self.result.text = text
        self.status.text = "Listening..."


class VoiceAssistantApp(App):
    def build(self):
        self.title = "Voice Assistant 811"
        return MainLayout()


if __name__ == "__main__":
    VoiceAssistantApp().run()
