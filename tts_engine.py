from jnius import autoclass, PythonJavaClass, java_method

PythonActivity = autoclass("org.kivy.android.PythonActivity")
TextToSpeech = autoclass("android.speech.tts.TextToSpeech")
Locale = autoclass("java.util.Locale")


class _TTSInitListener(PythonJavaClass):
    __javainterfaces__ = ["android/speech/tts/TextToSpeech$OnInitListener"]

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    @java_method("(I)V")
    def onInit(self, status):
        self.engine.ready = True


class TTSEngine:
    def __init__(self, language="en_US"):
        self.language = language
        self.ready = False
        self.listener = _TTSInitListener(self)
        self.tts = TextToSpeech(PythonActivity.mActivity, self.listener)

    def speak(self, text):
        if not self.ready or not self.tts:
            return False

        try:
            if self.language.startswith("ar"):
                self.tts.setLanguage(Locale("ar"))
            else:
                self.tts.setLanguage(Locale.US)

            self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, "811")
            return True
        except Exception:
            return False

    def stop(self):
        try:
            if self.tts:
                self.tts.stop()
                self.tts.shutdown()
        except Exception:
            pass
