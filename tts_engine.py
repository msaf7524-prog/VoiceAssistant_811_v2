from kivy.utils import platform

if platform == "android":
    try:
        from jnius import autoclass, PythonJavaClass, java_method

        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        TextToSpeech = autoclass("android.speech.tts.TextToSpeech")
        Locale = autoclass("java.util.Locale")
        HAS_ANDROID = True
    except Exception as e:
        print("Android TTS Imports Error:", e)
        HAS_ANDROID = False
else:
    HAS_ANDROID = False


if HAS_ANDROID:
    class _TTSInitListener(PythonJavaClass):
        __javainterfaces__ = [
            "android/speech/tts/TextToSpeech$OnInitListener"
        ]

        def __init__(self, engine):
            super().__init__()
            self.engine = engine

        @java_method("(I)V")
        def onInit(self, status):
            if status == TextToSpeech.SUCCESS:
                try:
                    # ضبط اللغة فور نجاح المبادأة
                    if self.engine.language.startswith("ar"):
                        self.engine.tts.setLanguage(Locale("ar"))
                    else:
                        self.engine.tts.setLanguage(Locale.US)
                except Exception as e:
                    print("TTS setLanguage Error:", e)
                self.engine.ready = True


class TTSEngine:

    def __init__(self, language="ar"):
        self.language = language
        self.ready = False
        self.tts = None
        self.listener = None

        if HAS_ANDROID:
            try:
                self.listener = _TTSInitListener(self)
                self.tts = TextToSpeech(
                    PythonActivity.mActivity,
                    self.listener
                )
            except Exception as e:
                print("TTS Init Error:", e)

    def speak(self, text):
        if not HAS_ANDROID or not self.ready or not self.tts:
            return False

        try:
            self.tts.speak(
                text,
                TextToSpeech.QUEUE_FLUSH,
                None,
                "VOICE811"
            )
            return True
        except Exception as e:
            print("TTS Speak Error:", e)
            return False

    def stop(self):
        if HAS_ANDROID and self.tts:
            try:
                self.tts.stop()
            except Exception:
                pass

    def shutdown(self):
        if HAS_ANDROID and self.tts:
            try:
                self.tts.shutdown()
            except Exception:
                pass
