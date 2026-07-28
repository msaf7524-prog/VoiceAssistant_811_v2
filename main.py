from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass, PythonJavaClass, java_method

PythonActivity = autoclass("org.kivy.android.PythonActivity")
TextToSpeech = autoclass("android.speech.tts.TextToSpeech")
Locale = autoclass("java.util.Locale")


class TTSListener(PythonJavaClass):
    __javainterfaces__ = ['android/speech/tts/TextToSpeech$OnInitListener']

    @java_method('(I)V')
    def onInit(self, status):
        pass


class VoiceApp(App):
    def build(self):
        self.listener = TTSListener()
        self.tts = TextToSpeech(PythonActivity.mActivity, self.listener)

        btn = Button(text="Start Assistant")
        btn.bind(on_press=self.speak)
        return btn

    def speak(self, instance):
        self.tts.setLanguage(Locale.US)
        self.tts.speak("Hello", 0, None)


VoiceApp().run()
