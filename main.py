from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

PythonActivity = autoclass("org.kivy.android.PythonActivity")
TextToSpeech = autoclass("android.speech.tts.TextToSpeech")
Locale = autoclass("java.util.Locale")


class VoiceApp(App):
    def build(self):
        self.activity = PythonActivity.mActivity
        self.tts = TextToSpeech(self.activity, None)
        self.tts.setLanguage(Locale.US)

        btn = Button(text="Start Assistant")
        btn.bind(on_press=self.speak)
        return btn

    def speak(self, instance):
        if self.tts is not None:
            self.tts.speak(
                "Hello, I am Voice Assistant 811",
                0,
                None
            )


VoiceApp().run()
