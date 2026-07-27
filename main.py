from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock

from jnius import autoclass

TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')
PythonActivity = autoclass('org.kivy.android.PythonActivity')


class VoiceApp(App):
    def build(self):
        self.tts = None
        btn = Button(text="Start Assistant")
        btn.bind(on_press=self.speak)
        Clock.schedule_once(self.init_tts, 0)
        return btn

    def init_tts(self, dt):
        activity = PythonActivity.mActivity
        self.tts = TextToSpeech(activity, None)
        self.tts.setLanguage(Locale.US)

    def speak(self, instance):
        if self.tts:
            self.tts.speak(
                "Hello, I am Voice Assistant 811",
                TextToSpeech.QUEUE_FLUSH,
                None,
                "test"
            )


VoiceApp().run()
